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

    # Name
    match = re.search(
        r"Technology\s*:\s*(.+)",
        text,
        re.IGNORECASE
    )

    if match:
        details["technology"] = match.group(1).strip()

    # Register Number
    match = re.search(
        r"\b[A-Z0-9]{6,20}\b",
        text,
        re.IGNORECASE
    )

    if match:
        details["register_no"] = match.group()

    # College
    match = re.search(
        r"College\s*:\s*(.+)",
        text,
        re.IGNORECASE
    )

    if match:
        details["college"] = match.group(1).strip()
    

    # Enrollment ID
    match = re.search(
        r"Enrollment ID:\s*([A-Za-z0-9]+)",
        text
    )
    if match:
        details["enrollment_id"] = match.group(1)

    # Technology
    match = re.search(
        r"Technology:\s*(.+)",
       text
    )

    if match:
        details["technology"] = match.group(1).strip()

    # Start Date
    match = re.search(
        r"Start Date:\s*([0-9]{2}-[A-Za-z]{3}-[0-9]{4})",
        text
    )
    if match:
        details["start_date"] = match.group(1)

    # End Date
    match = re.search(
        r"End Date:\s*([0-9]{2}-[A-Za-z]{3}-[0-9]{4})",
        text
    )
    if match:
        details["end_date"] = match.group(1)

    return details