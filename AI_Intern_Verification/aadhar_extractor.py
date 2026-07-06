import re

def extract_aadhar_details(text_list):

    details = {
        "name": "",
        "year_of_birth": "",
        "gender": "",
        "aadhar_number": ""
    }

    text = "\n".join(text_list)

    # Aadhaar Number
    aadhaar_pattern = re.search(
        r"(\d{4})\s+(\d{4})\s+(\d{4})",
        text
    )

    if aadhaar_pattern:
        details["aadhar_number"] = (
            aadhaar_pattern.group(1)
            + " "
            + aadhaar_pattern.group(2)
            + " "
            + aadhaar_pattern.group(3)
        )

        
    print(
        "Aadhaar Number:",
        details["aadhar_number"]
    )

    # Year of Birth
    yob = re.search(
        r"(19|20)\d{2}",
        text
    )

    if yob:
        details["year_of_birth"] = yob.group()

    # Gender
    if "Male" in text:
        details["gender"] = "Male"

    elif "Female" in text:
        details["gender"] = "Female"

    # Name
    for line in text_list:

        line = line.strip()

        if (
            "Government" not in line
            and "India" not in line
            and "Father" not in line
            and len(line) > 5
            and not any(char.isdigit() for char in line)
        ):
            details["name"] = line
            break

    return details

    print(text_list)