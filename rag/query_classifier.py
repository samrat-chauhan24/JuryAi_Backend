def detect_acts(query: str):

    q = query.lower()

    acts = []

    # -------------------------
    # CONSTITUTION
    # -------------------------

    constitution_keywords = [

        "constitution",
        "constitutional",

        "article",

        "fundamental rights",
        "fundamental right",

        "equality",
        "right to equality",

        "freedom of speech",
        "freedom of expression",

        "right to life",
        "right to liberty",
        "privacy as a fundamental right",

        "religious freedom",
        "freedom of religion",

        "directive principles",
        "dpsp",

        "writ",
        "habeas corpus",
        "mandamus",
        "certiorari",
        "quo warranto",
        "prohibition",

        "article 14",
        "article 15",
        "article 16",
        "article 19",
        "article 21",
        "article 25",
        "article 32",
        "article 226"
    ]

    # -------------------------
    # DPDP
    # -------------------------

    dpdp_keywords = [

        "dpdp",
        "data protection",

        "personal data",
        "sensitive personal data",

        "data fiduciary",
        "data principal",

        "consent",
        "consent manager",

        "data breach",
        "privacy breach",

        "data processing",
        "processing personal data",

        "right to correction",
        "right to erasure",

        "notice",

        "children data",
        "minor data",

        "cross border transfer",

        "data retention",

        "privacy policy",

        "privacy"
    ]

    # -------------------------
    # IT ACT
    # -------------------------

    it_act_keywords = [

        "it act",
        "information technology act",

        "cyber crime",
        "cybercrime",

        "hacking",
        "unauthorized access",

        "computer resource",

        "electronic record",
        "electronic signature",

        "digital signature",

        "intermediary",

        "website blocking",
        "blocking order",

        "interception",
        "monitoring",
        "decryption",

        "section 66",
        "section 67",
        "section 69",
        "section 72",

        "phishing",
        "malware",
        "ransomware",

        "cyber security",
        "cybersecurity"
    ]

    # -------------------------
    # BNS
    # -------------------------

    bns_keywords = [

        "murder",
        "attempt to murder",

        "culpable homicide",

        "hurt",
        "grievous hurt",

        "assault",

        "kidnapping",
        "abduction",

        "rape",
        "sexual assault",

        "criminal intimidation",

        "theft",
        "robbery",
        "dacoity",

        "extortion",

        "cheating",
        "fraud",

        "forgery",

        "criminal breach of trust",

        "offence",
        "offense",

        "punishment",

        "imprisonment",

        "bns",
        "bharatiya nyaya sanhita"
    ]

    # -------------------------
    # BNSS
    # -------------------------

    bnss_keywords = [

        "bnss",

        "arrest",
        "police arrest",

        "bail",
        "anticipatory bail",

        "fir",

        "investigation",

        "search warrant",

        "summons",

        "charge sheet",

        "criminal procedure",

        "remand",

        "cognizable offence",
        "non cognizable offence",

        "bharatiya nagarik suraksha sanhita"
    ]

    # -------------------------
    # BSA
    # -------------------------

    bsa_keywords = [

        "evidence",

        "burden of proof",

        "admissibility",

        "witness",

        "expert witness",

        "electronic evidence",

        "documentary evidence",

        "oral evidence",

        "proof",

        "presumption",

        "bharatiya sakshya adhiniyam",

        "bsa"
    ]

    if any(k in q for k in constitution_keywords):
        acts.append("constitution")

    if any(k in q for k in dpdp_keywords):
        acts.append("dpdp")

    if any(k in q for k in it_act_keywords):
        acts.append("it_act")

    if any(k in q for k in bns_keywords):
        acts.append("bns")

    if any(k in q for k in bnss_keywords):
        acts.append("bnss")

    if any(k in q for k in bsa_keywords):
        acts.append("bsa")

    return list(set(acts))