import re


# -------------------------------
# Extract Candidate Name
# -------------------------------
import re

def extract_name(text):

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    ignore = [
        "resume",
        "curriculum vitae",
        "linkedin",
        "email",
        "mobile",
        "phone",
        "objective",
        "education",
        "skills",
        "projects",
        "experience",
        "declaration",
        "technical",
        "strength",
        "place",
        "date"
    ]

    for line in lines[:10]:

        lower = line.lower()

        if any(word in lower for word in ignore):
            continue

        # remove degree after comma
        line = line.split(",")[0]

        # remove text inside brackets
        line = re.sub(r"\(.*?\)", "", line)

        line = line.strip()

        words = line.split()

        if 1 <= len(words) <= 4:

            if all(word.isalpha() for word in words):

                return " ".join(word.title() for word in words)

    return ""
# -------------------------------
# Extract Email
# -------------------------------
def extract_email(text):

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -------------------------------
# Extract Phone
# -------------------------------
def extract_phone(text):

    pattern = r'(\+91[\s-]?\d{10}|\d{10})'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -------------------------------
# Extract College
# -------------------------------
def extract_college(text):

    lines = text.split("\n")

    keywords = [
        "college",
        "university",
        "institute"
    ]

    for line in lines:

        lower = line.lower()

        if any(word in lower for word in keywords):

            return line.strip()

    return "Not Found"