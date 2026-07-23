import re

def extract_name(text):

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line

    return "Not Found"


def extract_email(text):

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"

def extract_phone(text):

    import re

    pattern = r'(\+91[\s-]?\d{10}|\d{10})'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_college(text):

    lines = text.split("\n")

    for line in lines:

        if "College" in line:
            return line.strip()

    return "Not Found"