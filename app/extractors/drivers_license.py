import re


def extract_drivers_license(text):

    fields = {}

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    for i, line in enumerate(lines):

        upper = line.upper()

        if upper == "KWON":

            fields["last_name"] = line

            if i + 1 < len(lines):
                fields["first_name"] = lines[i + 1]

        if "CUSTOMER NUMBER" in upper:

            if i + 1 < len(lines):
                fields["document_number"] = lines[i + 1]

        if "DATE OF BIRTH" in upper:

            if i + 1 < len(lines):
                fields["date_of_birth"] = lines[i + 1]

        if upper == "EXP":

            if i + 1 < len(lines):
                fields["expiration_date"] = lines[i + 1]

    return fields