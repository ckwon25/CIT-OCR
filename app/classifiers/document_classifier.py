def classify_document(text):

    text = text.upper()

    scores = {
        "drivers_license": 0,
        "social_security_card": 0,
        "passport": 0,
        "birth_certificate": 0,
        "naturalization_certificate": 0
    }

    if "DRIVER" in text:
        scores["drivers_license"] += 5

    if "LICENSE" in text:
        scores["drivers_license"] += 5

    if "SOCIAL SECURITY" in text:
        scores["social_security_card"] += 10

    if "PASSPORT" in text:
        scores["passport"] += 10

    if "BIRTH CERTIFICATE" in text:
        scores["birth_certificate"] += 10

    if "CERTIFICATE OF NATURALIZATION" in text:
        scores["naturalization_certificate"] += 10

    best_doc = max(scores, key=scores.get)

    confidence = scores[best_doc] / 10

    return {
        "document_type": best_doc,
        "confidence": round(confidence, 2)
    }