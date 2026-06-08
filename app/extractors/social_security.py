import re


def extract_social_security(text):

    fields = {}

    ssn_match = re.search(
        r"\d{3}-\d{2}-\d{4}",
        text
    )

    if ssn_match:
        fields["ssn"] = ssn_match.group()

    lines = text.split("\n")

    for line in lines:

        if line.strip().isupper():

            if len(line.split()) >= 2:

                if "SOCIAL" not in line:
                    if "SECURITY" not in line:
                        fields["name"] = line.strip()
                        break

    return fields
