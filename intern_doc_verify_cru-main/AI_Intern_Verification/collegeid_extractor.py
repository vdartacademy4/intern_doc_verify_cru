import re


def extract_collegeid_details(text_list):

    details = {
        "name": "",
        "reg_no": "",
        "college": ""
    }

    clean = []

    for line in text_list:

        line = line.strip()

        if line:
            clean.append(line)

    text_list = clean

    # -------------------------
    # NAME
    # -------------------------

    for line in text_list:

        lower = line.lower()

        if "name" in lower:

            line = re.sub(
                r"name\s*[:\-]?",
                "",
                line,
                flags=re.I
            )

            details["name"] = line.strip()

            break

    # -------------------------
    # COLLEGE
    # -------------------------

    for line in text_list:

        lower = line.lower()

        if (
            "engineering college" in lower
            or "college" in lower
            or "university" in lower
            or "institute" in lower
        ):

            if lower != "college id":

                details["college"] = line.strip()

                break

    # -------------------------
    # REGISTER NUMBER
    # -------------------------

    for line in text_list:

        # OCR mistake correction
        line = line.replace("Feg", "Reg")
        line = line.replace("I", "1")
        line = line.replace("O", "0")

        match = re.search(
            r"[0-9]{2}[A-Z]{2,6}[0-9]{3,6}",
            line,
            re.I
        )

        if match:

            details["reg_no"] = match.group()

            break

    print("COLLEGE ID DETAILS:", details)

    return details