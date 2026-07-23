import re


def extract_email_body_details(file_path):

    details = {
        "name": "",
        "register_no": "",
        "domain": "",
        "start_date": "",
        "end_date": ""
    }

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Name
    match = re.search(
        r"(?:Name|Candidate Name|Student Name)\s*:\s*(.*)",
        text,
        re.I
    )

    if match:
        details["name"] = match.group(1).strip()

    # Register Number
    match = re.search(
        r"(?:Register Number|Register No|Reg No)\s*:\s*(.*)",
        text,
        re.I
    )

    if match:
        details["register_no"] = match.group(1).strip()

    # Domain
    match = re.search(
        r"(?:Domain|Technology)\s*:\s*(.*)",
        text,
        re.I
    )

    if match:
        details["domain"] = match.group(1).strip()

    # Start Date
    match = re.search(
        r"(?:Start Date|Joining Date)\s*:\s*(.*)",
        text,
        re.I
    )

    if match:
        details["start_date"] = match.group(1).strip()

    # End Date
    match = re.search(
        r"(?:End Date|Completion Date)\s*:\s*(.*)",
        text,
        re.I
    )

    if match:
        details["end_date"] = match.group(1).strip()

    return details