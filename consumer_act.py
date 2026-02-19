"""
Consumer Protection Act 2019 - Extended Knowledge Base
This module contains an extensive, structured breakdown of the Indian Consumer Protection Act 2019.
It is designed to be imported into AI applications for Legal RAG (Retrieval-Augmented Generation).
"""

ACT_METADATA = {
    "title": "The Consumer Protection Act, 2019",
    "enforced_on": "July 20, 2020",
    "objective": "To provide for protection of the interests of consumers and to establish authorities for timely and effective administration and settlement of consumers' disputes.",
    "key_upgrade": "Replaced the 1986 Act to include E-commerce, Product Liability, Alternate Dispute Resolution (Mediation), and the establishment of the CCPA.",
}

# ─────────────────────────────────────────────────────────────────────────────
# KEY DEFINITIONS (Chapter I)
# ─────────────────────────────────────────────────────────────────────────────
DEFINITIONS = {
    "Section 2(1) - Advertisement": (
        "Any audio or visual publicity, representation, endorsement or pronouncement made by means of light, "
        "sound, smoke, gas, print, electronic media, internet or website and includes any notice, circular, label, wrapper, invoice or such other documents."
    ),
    "Section 2(7) - Consumer": (
        "Any person who buys goods or hires/avails services for a consideration. "
        "Includes offline, online, electronic, teleshopping, or multi-level marketing. "
        "Excludes persons who obtain goods for resale or commercial purposes."
    ),
    "Section 2(10) - Defect": (
        "Any fault, imperfection, or shortcoming in the quality, quantity, potency, purity, or standard "
        "which is required to be maintained by or under any law, or under any contract."
    ),
    "Section 2(11) - Deficiency": (
        "Any fault, imperfection, shortcoming, or inadequacy in the quality, nature, and manner of performance "
        "of a service. Includes acts of negligence, omission, or withholding relevant information."
    ),
    "Section 2(16) - E-Commerce": (
        "Buying or selling of goods or services, including digital products, over a digital or electronic network."
    ),
    "Section 2(41) - Restrictive Trade Practice": (
        "A trade practice which tends to bring about manipulation of price or its conditions of delivery or to affect "
        "flow of supplies in the market relating to goods or services in such a manner as to impose on the consumers "
        "unjustified costs or restrictions. Includes tie-up sales and delaying supplies."
    ),
    "Section 2(47) - Unfair Trade Practice": (
        "A trade practice which promotes the sale, use, or supply of any goods or services by adopting "
        "any unfair method or deceptive practice. Includes false representation, misleading advertisements, "
        "refusal to take back defective goods, and disclosing personal information confidentially given."
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# CENTRAL CONSUMER PROTECTION AUTHORITY (Chapter III)
# ─────────────────────────────────────────────────────────────────────────────
CCPA_CLAUSES = {
    "Section 10 - Establishment": "Establishment of the CCPA to regulate matters relating to violation of rights of consumers, unfair trade practices, and false or misleading advertisements.",
    "Section 15 - Investigation": "CCPA has an Investigation Wing headed by a Director General to conduct inquiries or investigations into consumer rights violations.",
    "Section 18 - Powers and Functions": "To protect and enforce the rights of consumers as a class, prevent unfair trade practices, ensure no false/misleading ads are made, and issue safety notices.",
    "Section 20 - Recalls and Refunds": "CCPA can order the recall of goods, withdrawal of services, reimbursement of the price paid, and discontinuation of unfair practices.",
    "Section 21 - Penalties for Misleading Ads": "CCPA can impose a penalty up to ₹10 Lakh on a manufacturer/endorser for a misleading ad. For subsequent violations, the penalty may extend to ₹50 Lakh. It can also prohibit the endorser from endorsing products for 1 to 3 years.",
    "Section 22 - Search and Seizure": "The Director General or authorized officers have the power to enter premises, search, and seize documents/records/articles if they suspect a violation of consumer rights.",
}

# ─────────────────────────────────────────────────────────────────────────────
# CONSUMER DISPUTES REDRESSAL COMMISSIONS (Chapter IV)
# ─────────────────────────────────────────────────────────────────────────────
# Note: Pecuniary limits updated as per Consumer Protection (Jurisdiction of the District Commission,
# the State Commission and the National Commission) Rules, 2021.
JURISDICTION = {
    "District Commission (DCDRC)": {
        "section": "Section 34",
        "pecuniary_limit": "Value of goods/services does not exceed ₹50 Lakh (Updated 2021).",
        "jurisdiction_area": "Where the opposite party resides/works, where the cause of action arises, OR where the complainant resides/personally works for gain (New addition in 2019 Act).",
        "appeal": "Appeals against District Commission orders lie with the State Commission within 45 days (Section 41) on questions of law or fact.",
    },
    "State Commission (SCDRC)": {
        "section": "Section 47",
        "pecuniary_limit": "Value of goods/services exceeds ₹50 Lakh but does not exceed ₹2 Crore (Updated 2021).",
        "jurisdiction_area": "Original jurisdiction for its pecuniary limit; appellate jurisdiction over District Commissions within the State.",
        "appeal": "Appeals against State Commission orders lie with the National Commission within 30 days (Section 51).",
    },
    "National Commission (NCDRC)": {
        "section": "Section 58",
        "pecuniary_limit": "Value of goods/services exceeds ₹2 Crore (Updated 2021).",
        "jurisdiction_area": "Original jurisdiction for its pecuniary limit; appellate jurisdiction over State Commissions across India.",
        "appeal": "Appeals against National Commission orders lie with the Supreme Court within 30 days (Section 67).",
    },
    "E-Filing": {
        "section": "Section 35",
        "details": "Consumers can file complaints electronically (E-Daakhil portal) and hearings can be conducted through video conferencing.",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# MEDIATION (Chapter V) - NEW IN 2019 ACT
# ─────────────────────────────────────────────────────────────────────────────
MEDIATION = {
    "Section 74 - Consumer Mediation Cell": "Establishment of Consumer Mediation Cells attached to District, State, and National Commissions.",
    "Section 79 - Settlement through Mediation": "If there is a scope for early settlement, the Commission may refer the dispute to mediation with the written consent of both parties.",
    "Section 81 - No Appeal": "If a dispute is resolved through mediation and a settlement agreement is signed, no appeal lies against such a settlement order.",
}

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCT LIABILITY (Chapter VI)
# ─────────────────────────────────────────────────────────────────────────────
PRODUCT_LIABILITY = {
    "Section 82 - Application": "Applies to all claims for compensation under product liability action.",
    "Section 83 - Action": "A product liability action may be brought by a complainant against a product manufacturer, product seller, or product service provider.",
    "Section 84 - Manufacturer Liability": "Manufacturer is liable if the product contains a manufacturing defect, design defect, deviates from manufacturing specifications, does not conform to the express warranty, or fails to contain adequate warnings (even if they prove they were not negligent).",
    "Section 85 - Service Provider Liability": "Liable if the service provided was faulty/imperfect/deficient, did not conform to express warranties, or lacked adequate warnings/instructions.",
    "Section 86 - Seller Liability": "Seller is liable if they exercised substantial control over designing/testing/packaging, altered/modified the product causing harm, made an express warranty independent of the manufacturer, or if the manufacturer is not identifiable/does not fall under Indian jurisdiction.",
    "Section 87 - Exceptions to Product Liability": "A product liability action will fail if the product was altered, modified, or misused by the consumer; or if the consumer failed to follow explicit warnings/instructions provided by the manufacturer.",
}

# ─────────────────────────────────────────────────────────────────────────────
# OFFENCES AND PENALTIES (Chapter VII)
# ─────────────────────────────────────────────────────────────────────────────
PENALTIES = {
    "Section 88 - Non-compliance of CCPA Directions": "Imprisonment up to 6 months, or fine up to ₹20 Lakh, or both.",
    "Section 89 - False/Misleading Ads": "Any manufacturer or service provider who causes a false/misleading ad shall be punished with imprisonment up to 2 years and a fine up to ₹10 Lakh. For subsequent offences: imprisonment up to 5 years and fine up to ₹50 Lakh.",
    "Section 90 - Adulterants": "Manufacturing/selling/distributing products containing adulterants:\n- No injury: Fine up to ₹1 Lakh, imprisonment up to 6 months.\n- Injury: Fine up to ₹3 Lakh, imprisonment up to 1 year.\n- Grievous hurt: Fine up to ₹5 Lakh, imprisonment up to 7 years.\n- Death: Fine up to ₹10 Lakh, minimum 7 years imprisonment (may extend to life).",
    "Section 91 - Spurious Goods": "Manufacturing/selling spurious goods carries identical punishments to Section 90 depending on the severity of the harm caused.",
    "Section 93 - Vexatious Search": "If the Director General or any authorized officer conducts a search without reasonable ground, they shall be punished with imprisonment up to 1 year, or fine up to ₹10,000, or both.",
}

# ─────────────────────────────────────────────────────────────────────────────
# E-COMMERCE RULES (Under Section 94) - Expanded 2020 Rules
# ─────────────────────────────────────────────────────────────────────────────
ECOMMERCE_RULES = {
    "Grievance Redressal": "Every e-commerce entity must appoint a nodal officer/grievance officer. The officer must acknowledge complaints within 48 hours and resolve them within 1 month.",
    "Information Disclosure": "Sellers must display the total price (including all charges), return/refund policies, warranty details, delivery conditions, and country of origin.",
    "Unfair Practices": "E-commerce platforms cannot manipulate prices (price gouging), impose unjustified cancellation charges, or refuse to take back defective/deficient goods.",
    "Marketplace vs. Inventory": "Rules differentiate between Marketplace e-commerce (like Amazon/Flipkart acting as facilitators) and Inventory e-commerce (where the platform owns the inventory). Marketplaces must require sellers to undertake that descriptions/images are accurate.",
    "Fall-back Liability": "If a seller registered on a marketplace e-commerce entity fails to deliver goods/services due to negligent conduct resulting in loss to the consumer, the marketplace may bear fall-back liability (subject to ongoing legal interpretations).",
}

# ─────────────────────────────────────────────────────────────────────────────
# HELPLINES AND AUTHORITY MAPPING
# ─────────────────────────────────────────────────────────────────────────────
COMPLAINT_CATEGORIES = {
    "Online Shopping": {
        "icon": "🛒",
        "authorities": ["Consumer Court (DCDRC)", "E-Commerce Grievance Officer"],
        "helpline": "1800-11-4000",
    },
    "Defective Product": {
        "icon": "🔧",
        "authorities": ["Consumer Court (DCDRC)", "Manufacturer / Brand"],
        "helpline": "1800-11-4000",
    },
    "Cyber Fraud": {
        "icon": "💻",
        "authorities": ["Cyber Crime Portal", "Cyber Cell (Police)"],
        "helpline": "1930",
    },
    "Banking Fraud": {
        "icon": "🏦",
        "authorities": ["RBI Ombudsman", "Banking Ombudsman"],
        "helpline": "14448 / 1930",
    },
    "Insurance": {
        "icon": "🛡️",
        "authorities": ["IRDAI Grievance Cell", "Insurance Ombudsman"],
        "helpline": "155255",
    },
    "Telecom Issue": {
        "icon": "📱",
        "authorities": ["TRAI Portal", "Service Provider Grievance"],
        "helpline": "1800-11-0040",
    },
    "Food Safety": {
        "icon": "🍽️",
        "authorities": ["FSSAI", "Local Health Authority"],
        "helpline": "1800-11-2100",
    },
    "Other Issue": {
        "icon": "⚖️",
        "authorities": ["Consumer Court (DCDRC)", "CCPA"],
        "helpline": "1800-11-4000",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# HELPER METHOD TO GENERATE STRING FOR LLM CONTEXT
# ─────────────────────────────────────────────────────────────────────────────
def get_act_context() -> str:
    """
    Returns a formatted string containing the entire Consumer Protection Act 2019
    breakdown, ready to be injected into an LLM's system prompt or RAG context window.
    """
    context = []
    context.append(f"--- {ACT_METADATA['title'].upper()} ---\n")
    context.append(f"Objective: {ACT_METADATA['objective']}")
    context.append(f"Key Upgrades: {ACT_METADATA['key_upgrade']}\n")

    context.append("1. KEY DEFINITIONS:")
    for key, value in DEFINITIONS.items():
        context.append(f"  • {key}: {value}")

    context.append("\n2. CENTRAL CONSUMER PROTECTION AUTHORITY (CCPA):")
    for key, value in CCPA_CLAUSES.items():
        context.append(f"  • {key}: {value}")

    context.append("\n3. JURISDICTION OF COMMISSIONS (2021 Updates):")
    for court, details in JURISDICTION.items():
        if "pecuniary_limit" in details:
            context.append(
                f"  • {court} ({details['section']}):\n"
                f"    - Limit: {details['pecuniary_limit']}\n"
                f"    - Area: {details['jurisdiction_area']}\n"
                f"    - Appeals: {details['appeal']}"
            )
        else:
            context.append(f"  • {court} ({details['section']}): {details['details']}")

    context.append("\n4. MEDIATION (CHAPTER V):")
    for key, value in MEDIATION.items():
        context.append(f"  • {key}: {value}")

    context.append("\n5. PRODUCT LIABILITY:")
    for key, value in PRODUCT_LIABILITY.items():
        context.append(f"  • {key}: {value}")

    context.append("\n6. OFFENCES AND PENALTIES:")
    for key, value in PENALTIES.items():
        context.append(f"  • {key}: {value}")

    context.append("\n7. E-COMMERCE RULES 2020:")
    for key, value in ECOMMERCE_RULES.items():
        context.append(f"  • {key}: {value}")

    return "\n".join(context)
