import os

# Supported formats
REQUIRED_FILES = {
    "resume": [".pdf"],
    "aadhar": [".jpg", ".jpeg", ".png", ".pdf"],
    "college_id": [".jpg", ".jpeg", ".png", ".pdf"],
    "offer_letter": [".pdf"],
    "photo": [".jpg", ".jpeg", ".png",".pdf"]
}


def check_required_files(candidate_folder):

    files = os.listdir(candidate_folder)

    found = {
        "resume": False,
        "aadhar": False,
        "college_id": False,
        "offer_letter": False,
        "photo": False
    }

    invalid_files = []

    for file in files:

        filename = file.lower()
        ext = os.path.splitext(filename)[1]

        # Resume
        if "resume" in filename:

            if ext in REQUIRED_FILES["resume"]:
                found["resume"] = True
            else:
                invalid_files.append(
                    f"{file} (Resume should be PDF)"
                )

        # Aadhaar
        elif "aadhar" in filename or "aadhaar" in filename:

            if ext in REQUIRED_FILES["aadhar"]:
                found["aadhar"] = True
            else:
                invalid_files.append(
                    f"{file} (Invalid Aadhaar format)"
                )

        # College ID
        elif "college" in filename:

            if ext in REQUIRED_FILES["college_id"]:
                found["college_id"] = True
            else:
                invalid_files.append(
                    f"{file} (Invalid College ID format)"
                )

        # Offer Letter
        elif "offer" in filename:

            if ext in REQUIRED_FILES["offer_letter"]:
                found["offer_letter"] = True
            else:
                invalid_files.append(
                    f"{file} (Offer Letter should be PDF)"
                )
        #photo
        elif "photo" in filename or "passport" in filename:

            if ext in REQUIRED_FILES["photo"]:
                found["photo"] = True
            else:
                invalid_files.append(
                f"{file} (Passport size photo should be JPG/PNG)"
                )

    missing = []

    for key in found:

        if not found[key]:
            missing.append(key)

    return missing, invalid_files


# ------------------------------------
# Used by app.py
# ------------------------------------
def check_documents(folder_path):

    return check_required_files(folder_path)