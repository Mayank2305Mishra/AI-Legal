import streamlit as st
from groq import Groq
from datetime import datetime
import json, io, re
from consumer_act import get_act_context, COMPLAINT_CATEGORIES

# ─────────────────────────────────────────────────────────────────────────────
# PDF HELPERS
# ─────────────────────────────────────────────────────────────────────────────


def extract_text_from_pdf(file_bytes: bytes):
    try:
        import pypdf
    except ImportError:
        return "", "pypdf not installed — run: pip install pypdf"
    try:
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        if not reader.pages:
            return "", "PDF has no pages."
        pages = []
        for i, page in enumerate(reader.pages):
            t = page.extract_text() or ""
            if t.strip():
                pages.append(f"[Page {i+1}]\n{t.strip()}")
        if not pages:
            return "", "No text found — PDF may be scanned/image-based."
        return "\n\n".join(pages), ""
    except Exception as e:
        return "", f"Could not read PDF: {e}"


def chunk_text(text: str, chunk_size=800, overlap=120):
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunks.append(" ".join(words[i : i + chunk_size]))
        i += chunk_size - overlap
    return chunks


def retrieve_context(query: str, pdf_store: dict, top_k=5) -> str:
    if not pdf_store:
        return ""
    q_words = {w for w in re.sub(r"[^\w\s]", "", query.lower()).split() if len(w) > 3}
    if not q_words:
        return ""
    hits = []
    for fname, chunks in pdf_store.items():
        for chunk in chunks:
            score = sum(1 for w in q_words if w in chunk.lower())
            if score:
                hits.append((score, fname, chunk))
    hits.sort(reverse=True, key=lambda x: x[0])
    if not hits:
        return ""
    lines = ["RELEVANT EXCERPTS FROM UPLOADED PDFs:"]
    for _, fname, chunk in hits[:top_k]:
        lines.append(f"\n--- Source: {fname} ---\n{chunk.strip()}")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AI Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# KNOWLEDGE BASE & DATA
# ─────────────────────────────────────────────────────────────────────────────

CONSUMER_RIGHTS_KB = get_act_context()


STEPS = ["Select Issue", "Describe", "Your Rights", "Draft Letter", "Submit"]

# ─────────────────────────────────────────────────────────────────────────────
# LLM
# ─────────────────────────────────────────────────────────────────────────────


@st.cache_resource
def get_client(api_key):
    return Groq(api_key=api_key)


def build_system_prompt(category, user_details, rag_context=""):
    cat = COMPLAINT_CATEGORIES.get(category, COMPLAINT_CATEGORIES["Other Issue"])
    rag_block = f"\nPDF CONTEXT:\n{rag_context}\n" if rag_context else ""
    return f"""You are an expert AI Legal Assistant specialising in Indian Consumer Protection Law.

KNOWLEDGE BASE:
{CONSUMER_RIGHTS_KB}
{rag_block}
CASE:
- Type: {category}
- Authorities: {', '.join(cat['authorities'])}
- Details: {json.dumps(user_details)}

YOUR ROLE:
Guide users to collect complaint details. Explain rights simply. Draft a formal letter. Be clear and supportive.
Mark the letter start with exactly: 📄 COMPLAINT LETTER DRAFT:
"""


def chat_with_groq(client, messages, system_prompt, model):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_prompt}] + messages,
        temperature=0.4,
        max_tokens=2048,
    )
    return r.choices[0].message.content


def extract_letter(text):
    marker = "📄 COMPLAINT LETTER DRAFT:"
    if marker in text:
        pre, letter = text.split(marker, 1)
        return pre.strip(), letter.strip()
    return text, None


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────


def init_session():
    defaults = {
        "messages": [],
        "category": None,
        "user_details": {},
        "letter_draft": None,
        "step": "select_category",
        "pdf_store": {},
        "pdf_errors": {},
        "chat_step": 1,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_session()

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("⚖️ Legal Assistant")
    st.caption("Consumer Rights Made Easy")

    api_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...")
    model_choice = st.selectbox(
        "Model",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
    )

    st.divider()

    st.subheader("📂 Upload PDFs")
    uploaded_files = st.file_uploader(
        "Drop Legal PDFs here", type=["pdf"], accept_multiple_files=True
    )

    if uploaded_files:
        for uf in uploaded_files:
            if uf.name in st.session_state["pdf_store"]:
                continue
            with st.spinner(f"Indexing {uf.name}…"):
                text, err = extract_text_from_pdf(uf.read())
            if err:
                st.session_state["pdf_errors"][uf.name] = err
            else:
                st.session_state["pdf_store"][uf.name] = chunk_text(text)
                st.session_state["pdf_errors"].pop(uf.name, None)

    for fname, err in st.session_state["pdf_errors"].items():
        st.error(f"{fname}: {err}")

    if st.session_state["pdf_store"]:
        st.success(f"{len(st.session_state['pdf_store'])} PDF(s) Indexed")
        if st.button("Clear All PDFs"):
            st.session_state["pdf_store"] = {}
            st.rerun()

    st.divider()
    if st.button("Start New Complaint", type="primary"):
        st.session_state.update(
            {
                "messages": [],
                "category": None,
                "user_details": {},
                "letter_draft": None,
                "step": "select_category",
                "chat_step": 1,
            }
        )
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# MAIN PAGE
# ─────────────────────────────────────────────────────────────────────────────

st.title("AI Legal Assistant")
st.caption("Know your rights · Draft your complaint · Get justice")

if st.session_state["pdf_store"]:
    st.info(
        f"RAG Active: Using knowledge from {len(st.session_state['pdf_store'])} uploaded documents."
    )

if not api_key:
    st.warning("Please enter your Groq API Key in the sidebar to begin.")
    st.stop()

try:
    client = get_client(api_key)
except Exception as e:
    st.error(f"API client error: {e}")
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: CATEGORY SELECTION
# ─────────────────────────────────────────────────────────────────────────────

if st.session_state["step"] == "select_category":
    st.progress(0)
    st.subheader("What type of complaint do you have?")

    cols = st.columns(4)
    for i, (cat_name, info) in enumerate(COMPLAINT_CATEGORIES.items()):
        with cols[i % 4]:
            if st.button(
                f"{info['icon']}  {cat_name}", key=f"cat_{i}", use_container_width=True
            ):
                st.session_state["category"] = cat_name
                st.session_state["step"] = "chat"
                st.session_state["chat_step"] = 2
                st.session_state["messages"] = [
                    {
                        "role": "assistant",
                        "content": f"Hello! I am ready to help with your **{cat_name}** complaint.\n\nPlease tell me:\n1. What happened?\n2. When did it happen?\n3. Which company is involved?",
                    }
                ]
                st.rerun()
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2-5: CHAT INTERFACE
# ─────────────────────────────────────────────────────────────────────────────

if st.session_state["step"] == "chat" and st.session_state["category"]:
    cat = st.session_state["category"]
    cat_info = COMPLAINT_CATEGORIES[cat]

    # Calculate Progress
    msg_count = len([m for m in st.session_state["messages"] if m["role"] == "user"])
    chat_step = (
        5
        if st.session_state.get("letter_draft")
        else (4 if msg_count >= 3 else (3 if msg_count >= 2 else 2))
    )

    # Progress Bar
    st.progress((chat_step - 1) / 4)
    st.caption(f"Step {chat_step} of 5: {STEPS[chat_step-1]}")

    # Header Info
    c1, c2 = st.columns([3, 1])
    with c1:
        st.subheader(f"{cat_info['icon']} {cat} Complaint")
    with c2:
        st.metric("Helpline", cat_info["helpline"])

    st.divider()


    # Chat History (Native Streamlit Components)
    for i, msg in enumerate(
        st.session_state["messages"]
    ):  # <-- Added enumerate(..) here
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant"):
                display_text, letter = extract_letter(msg["content"])
                st.write(display_text)
                if letter:
                    # Added unique keys using the loop index 'i'
                    st.text_area("Draft Letter", letter, height=300, key=f"draft_{i}")
                    st.download_button(
                        "Download Letter (.txt)",
                        data=letter,
                        file_name="complaint_letter.txt",
                        key=f"dl_{i}",  # <-- Unique key here
                    )
    # Chat Input
    if prompt := st.chat_input("Describe your issue..."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.rerun()

    # If the last message was from the user, generate response
    if (
        st.session_state["messages"]
        and st.session_state["messages"][-1]["role"] == "user"
    ):
        with st.chat_message("assistant"):
            with st.spinner("Analysing legal context..."):
                try:
                    rag_ctx = retrieve_context(
                        st.session_state["messages"][-1]["content"],
                        st.session_state["pdf_store"],
                    )
                    sys_p = build_system_prompt(
                        cat, st.session_state["user_details"], rag_ctx
                    )
                    response = chat_with_groq(
                        client, st.session_state["messages"], sys_p, model_choice
                    )

                    st.write(
                        extract_letter(response)[0]
                    )  # Write the text part immediately

                    st.session_state["messages"].append(
                        {"role": "assistant", "content": response}
                    )

                    _, letter = extract_letter(response)
                    if letter:
                        st.session_state["letter_draft"] = letter
                        st.rerun()  # Rerun to show the letter in the history loop properly

                except Exception as exc:
                    st.error(f"Error: {exc}")

    # Helper Buttons
    st.divider()
    col1, col2, col3 = st.columns(3)
    if col1.button("📄 Draft Letter Now"):
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": "Please draft the formal complaint letter based on what I have told you.",
            }
        )
        st.rerun()
    if col2.button("⚖️ Explain My Rights"):
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": "What are my specific legal rights in this situation?",
            }
        )
        st.rerun()
    if col3.button("🏛️ Where to Submit?"):
        st.session_state["messages"].append(
            {"role": "user", "content": "Where exactly do I file this complaint?"}
        )
        st.rerun()
