import re


def extract_aadhar_details(text):

    # Convert list to string if needed
    if isinstance(text, list):
        text = "\n".join(text)

    details = {
        "name": "",
        "year_of_birth": "",
        "gender": "",
        "aadhar_number": ""
    }

    # -------------------------
    # Aadhaar Number
    # -------------------------
    numbers = re.findall(r"\b\d{4}\s\d{4}\s\d{4}\b", text)

    if numbers:
        details["aadhar_number"] = numbers[0]
    else:
        digits = re.findall(r"\d", text)
        if len(digits) >= 12:
            num = "".join(digits[-12:])
            details["aadhar_number"] = (
                f"{num[:4]} {num[4:8]} {num[8:]}"
            )

    # -------------------------
    # DOB / Year
    # -------------------------
    dob = re.search(
        r"DOB\s*[:.]?\s*(\d{2}/\d{2}/\d{4})",
        text,
        re.IGNORECASE
    )

    if dob:
        details["year_of_birth"] = dob.group(1)
    else:
        year = re.search(r"\b(19|20)\d{2}\b", text)
        if year:
            details["year_of_birth"] = year.group()

    # -------------------------
    # Gender
    # -------------------------
    if re.search(r"\bMale\b", text, re.IGNORECASE):
        details["gender"] = "Male"

    elif re.search(r"\bFemale\b", text, re.IGNORECASE):
        details["gender"] = "Female"

    # -------------------------
    # Name
    # -------------------------

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    ignore_words = [
        "government",
        "india",
        "aadhaar",
        "unique",
        "authority",
        "enrollment",
        "address",
        "male",
        "female",
        "dob",
        "proof",
        "identity",
        "mobile",
        "uidai",
        "information",
        "your aadhaar",
        "to",
        "pin code",
        "district",
        "state",
        "sub district",
        "vtc",
        "po",
        "s/o"
    ]

    for line in lines:

        lower = line.lower()

        if any(word in lower for word in ignore_words):
            continue

        if re.search(r"\d", line):
            continue

        if re.fullmatch(r"[A-Za-z ]{5,}", line):

            words = line.split()

            if 2 <= len(words) <= 4:

                uppercase = sum(word.isupper() for word in words)

                if uppercase == len(words):
                    continue

                details["name"] = line
                break

    print("\nAADHAAR DETAILS")
    print(details)

    return details