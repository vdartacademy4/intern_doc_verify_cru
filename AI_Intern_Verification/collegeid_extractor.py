import re

def extract_collegeid_details(text_list):

    details = {
        "name": "",
        "reg_no": "",
        "college": ""
    }

    clean_text = []

    for line in text_list:

        line = line.strip()

        if line:

            clean_text.append(line)

    text_list = clean_text

    # Name

    possible_names = []

    for line in text_list:

        line = line.strip()

        if len(line) < 5:
            continue

        if any(ch.isdigit() for ch in line):
            continue

        lower = line.lower()

        if any(word in lower for word in [

            "college",
            "engineering",
            "engg",
            "technology",
            "polytechnic",
            "university",
            "institution",
            "autonomous",
            "principal",
            "director",
            "student",
            "identity",
            "card",
            "id",
            "approved",
            "affiliated",
            "naac",
            "aicte",
            "www",
            "http"
            "admission",
            "admit",
            "office",
            "dean",
            "faculty",
            "branch",
            "course",
            "semester",
            "batch",
            "year",
            "session"

        ]):
            continue

        possible_names.append(line)

    print("Possible Names:", possible_names)

    best_name = ""
    best_score = -1

    for candidate in possible_names:

        score = 0

        words = candidate.split()

        if 2 <= len(words) <= 5:
            score += 30

        if candidate.istitle() or candidate.isupper():
            score += 20

        if all(word.isalpha() for word in words):
            score += 30

        if len(candidate) > 8:
            score += 20

        if score > best_score:
            best_score = score
            best_name = candidate

    details["name"] = best_name

    # College Name

    college_keywords = [
        "college",
        "engineering",
        "technology",
        "institute",
        "university",
        "polytechnic"
    ]

    college = ""

    for i, line in enumerate(text_list):

        lower = line.lower()

        if any(word in lower for word in [
            "college",
            "engineering",
            "engg",
            "technology",
            "university",
            "institute"
        ]):

            college = line

            if i > 0:

                previous = text_list[i-1].strip()

                if len(previous) > 2:

                    college = previous + " " + line

            break

    details["college"] = college


    # Register Number

    for line in text_list:

        line = line.strip()

        match = re.search(

            r"\b([A-Z]{1,5}\d{2,15}[A-Z0-9]*)\b"
            r"|\b\d{8,15}\b",

            line,
            re.I

        )   

        if match:

            value = match.group()

            if any(c.isdigit() for c in value):

                details["reg_no"] = value

                break
    
    print("COLLEGE ID DETAILS:", details)

    return details