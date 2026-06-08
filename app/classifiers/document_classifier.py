def classify_document(text):

    text = text.upper()

    scores = {
        "social_security_card": 0,
        "passport": 0,
        "birth_certificate": 0,
        "naturalization_certificate": 0,
        "certificate_of_citizenship": 0,
        "green_card": 0,
        "drivers_license": 0
    }

    if "SOCIAL SECURITY" in text:
        scores["social_security_card"] += 10

    if "UNITED STATES PASSPORT" in text:
        scores["passport"] += 10

    if "CERTIFICATE OF NATURALIZATION" in text:
        scores["naturalization_certificate"] += 10

    if "CERTIFICATE OF CITIZENSHIP" in text:
        scores["certificate_of_citizenship"] += 10

    if "BIRTH CERTIFICATE" in text:
        scores["birth_certificate"] += 10

    best_doc = max(scores, key=scores.get)

    confidence = scores[best_doc] / 10

    if confidence == 0:
        return {
            "document_type": "unknown",
            "confidence": 0
        }

    return {
        "document_type": best_doc,
        "confidence": round(confidence, 2)
    }
