import pdfplumber
import re

def extract_offer_details(pdf_path):

    details = {
        "name": "",
        "college": "",
        "register_no": "",
        "enrollment_id": "",
        "technology": "",
        "start_date": "",
        "end_date": ""
    }

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    print("\n========== OFFER LETTER TEXT ==========")
    print(text)
    print("======================================")

    # Name
    match = re.search(
    r"Dear\s+([A-Za-z ]+)",
    text,
    re.IGNORECASE
    )

    if match:
        details["name"] = match.group(1).strip()

    # Enrollment ID
    match = re.search(
    r"Enrollment\s*ID\s*[:\-]?\s*([A-Za-z0-9]+)",
    text,
    re.IGNORECASE
    )

    if match:
        details["enrollment_id"] = match.group(1)
    # Technology
    
    
    match = re.search(
        r"Technology\s*:\s*(.*?)(?:Domain\s*:|Organization\s*:|Location\s*:|Start\s*Date\s*:)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        details["technology"] = " ".join(match.group(1).split())
    # Start Date
    match = re.search(
    r"Start\s*Date\s*:\s*([0-9]{2}-[A-Za-z]{3}-[0-9]{4})",
    text,
    re.IGNORECASE
    )

    if match:
        details["start_date"] = match.group(1)

    # End Date
    match = re.search(
    r"End\s*Date\s*:\s*([0-9]{2}-[A-Za-z]{3}-[0-9]{4})",
    text,
    re.IGNORECASE
    )

    if match:
        details["end_date"] = match.group(1)

    return details