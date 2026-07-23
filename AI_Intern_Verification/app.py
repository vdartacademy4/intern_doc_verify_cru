import os
import pdfplumber

from email_fetcher import fetch_emails
from csv_manager import save_to_csv

from ocr_processor import extract_text_from_image
from aadhar_extractor import extract_aadhar_details
from collegeid_extractor import extract_collegeid_details
from offerletter_extractor import extract_offer_details
from email_body_extractor import extract_email_body_details

from verification_engine import verify_all_names
from document_checker import check_documents

from extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_college
)


# -------------------------------
# STEP 
# -------------------------------
def run_pipeline():

    folders = os.listdir("uploads")

    for folder_name in folders:

        folder_path = os.path.join("uploads", folder_name)

        if not os.path.isdir(folder_path):
            continue

        print("\n==============================")
        print("Processing:", folder_name)
        print("==============================")

        # -------------------------------
        # STEP 3: RESUME EXTRACTION
        # -------------------------------
        resume_path = f"{folder_path}/resume.pdf"


        if not os.path.exists(resume_path):

            print("Resume Missing")

            os.makedirs("rejected", exist_ok=True)

            os.rename(
                folder_path,
                f"rejected/{folder_name}"
            )

            continue

        text = ""

        try:
            with pdfplumber.open(resume_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print("Resume error:", e)
            continue

        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        college = extract_college(text)

        print("\nRESUME DETAILS")
        print("Name :", name)
        print("Email:", email)
        print("Phone:", phone)
        print("College:", college)

        # -------------------------------
        # STEP 4: AADHAAR EXTRACTION
        # -------------------------------
        aadhar_path = f"{folder_path}/aadhar.jpg"

        aadhar_name = ""

        aadhar_details = {
            "name": "",
            "year_of_birth": "",
            "gender": "",
            "aadhar_number": ""
        }

        if os.path.exists(aadhar_path):

            aadhar_text = extract_text_from_image(
                aadhar_path
            )

            aadhar_details = extract_aadhar_details(
                aadhar_text
            )

            aadhar_name = aadhar_details["name"]

        else:

            print("\nAADHAAR NOT FOUND")



        

        # -------------------------------
        # STEP 5: COLLEGE ID EXTRACTION
        # -------------------------------
        college_name = ""

        collegeid_details = {
            "college": "",
            "reg_no": "",
            "name": ""
        }

        collegeid_path = f"{folder_path}/collegeid.jpg"

        if os.path.exists(collegeid_path):

            collegeid_text = extract_text_from_image(collegeid_path)

            print("\nRAW COLLEGE ID OCR")
            print(collegeid_text)

            collegeid_details = extract_collegeid_details(
                collegeid_text
            )

            college_name = collegeid_details["name"]

            print("\nCOLLEGE ID FOUND")

        else:

            print("\nCOLLEGE ID NOT FOUND")

        
        # -------------------------------
        # STEP 5.5: OFFER LETTER EXTRACTION
        # -------------------------------

        offer_details = {
            "name": "",
            "register_no": "",
            "college": "",
            "technology": "",
            "enrollment_id": "",
            "start_date": "",
            "end_date": ""
        }

        offer_path = f"{folder_path}/offerletter.pdf"

        if os.path.exists(offer_path):

            print("\nOFFER LETTER FOUND")

            offer_details = extract_offer_details(
                offer_path
                )

            print("Name :", offer_details["name"])
            print("Enrollment ID :", offer_details["enrollment_id"])
            print("Technology :", offer_details["technology"])
            print("Start Date :", offer_details["start_date"])
            print("End Date :", offer_details["end_date"])

        else:

            print("\nOFFER LETTER NOT FOUND")



        email_details = {
            "name": "",
            "register_no": "",
            "domain": "",
            "start_date": "",
            "end_date": ""
        }

        email_body_path = f"{folder_path}/email_body.txt"

        if os.path.exists(email_body_path):

            email_details = extract_email_body_details(
                email_body_path
            )

            print("\nEMAIL BODY DETAILS")

            print("Name :", email_details["name"])
            print("Register No :", email_details["register_no"])
            print("Domain :", email_details["domain"])
            print("Start Date :", email_details["start_date"])
            print("End Date :", email_details["end_date"])

            master_name = email_details["name"].upper().strip()

        else:

            print("\nEMAIL BODY NOT FOUND")

            master_name = ""


        # -------------------------------
        # STEP 6: DOCUMENT CHECK
        # -------------------------------
        missing_docs = check_documents(folder_path)

        # -------------------------------
        # STEP 7: VERIFICATION
        # -------------------------------
        

        if (
            master_name and
            name and
            aadhar_name and
            college_name and
            offer_details["name"]
        ):

            result = verify_all_names(
                master_name,
                name,
                aadhar_name,
                college_name,
                offer_details["name"]
            )

        else:

            result = {
                "resume_status": "MISSING",
                "aadhar_status": "MISSING",
                "college_status": "MISSING",
                "offer_status": "MISSING",
                "status": "MANUAL REVIEW",
                "score": 0
            }

        print("\nFINAL VERIFICATION")
        print("STATUS:", result["status"])
        print("SCORE:", result["score"])

        uploaded_files = ", ".join(
            os.listdir(folder_path)
        )

        # -------------------------------
        # STEP 8: SAVE CSV
        # -------------------------------
        save_to_csv(
           folder_name,
            master_name,

            result["resume_status"],
            result["aadhar_status"],
            result["college_status"],
            result["offer_status"],

            email,
            phone,

            collegeid_details["college"],
            email_details["register_no"],
            aadhar_details["aadhar_number"],

            offer_details["technology"],

            offer_details["enrollment_id"],
            offer_details["start_date"],
            offer_details["end_date"],

            uploaded_files,
            ", ".join(missing_docs),

            result["status"]
        )

        # Move processed folder
        os.makedirs("processed", exist_ok=True)

        processed_folder = os.path.join(
            "processed",
            folder_name
        )

        os.rename(
            folder_path,
            processed_folder
        )

        print("Moved to processed folder")


# -------------------------------
# MAIN RUN
# -------------------------------


if __name__ == "__main__":

    files = fetch_emails()

    print("\nEMAIL FILES DOWNLOADED")

    for file in files:
        print(file)

    print("\nDOWNLOADED FILES:")
    print(files)

    run_pipeline()




print("\n==============================")
print("PROCESS COMPLETED SUCCESSFULLY")
print("==============================")