import os
import pdfplumber
import re
import shutil

from email_fetcher import fetch_emails
from csv_manager import save_to_csv

from ocr_processor import extract_text_from_image
from aadhar_extractor import extract_aadhar_details
from collegeid_extractor import extract_collegeid_details
from offerletter_extractor import extract_offer_details
from email_body_extractor import extract_email_body_details
from photo_verifier import verify_photo

from verification_engine import verify_all_names
from document_checker import check_documents
from document_checker import check_required_files
from mailer import send_missing_document_mail
from extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_college
)

    

# -------------------------------
# STEP 
# -------------------------------
def run_pipeline(candidates):

    for candidate in candidates:

        folder_name = candidate["folder_name"]
        folder_path = candidate["folder_path"]
        sender_email = candidate["sender_email"]

        if not os.path.isdir(folder_path):
            continue

        missing, invalid_files = check_required_files(folder_path)

        if missing or invalid_files:

            print("\nDOCUMENT CHECK")

            if missing:
                print("Missing Documents:")
                for doc in missing:
                    print("-", doc)

            if invalid_files:
                print("\nInvalid Files:")
                for file in invalid_files:
                    print("-", file)

            save_to_csv(
                folder_name,
                "",
                "MISSING",
                "MISSING",
                "MISSING",
                "MISSING",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ", ".join(missing + invalid_files),
                "INVALID / MISSING DOCUMENTS"
            )

            if missing or invalid_files:

                send_missing_document_mail(
                    sender_email,
                    missing + invalid_files
                )
            print("Continuing with document extraction")
        print("\n==============================")
        print("Processing:", folder_name)
        print("==============================")

        # -------------------------------
        # STEP 3 : RESUME EXTRACTION
        # -------------------------------

        name = ""
        email = ""
        phone = ""
        college = ""

        resume_path = os.path.join(folder_path, "resume.pdf")

        if os.path.exists(resume_path):

            text = ""

            try:

                with pdfplumber.open(resume_path) as pdf:

                    for page in pdf.pages:

                        page_text = page.extract_text()

                        if page_text:
                            text += page_text + "\n"

                name = extract_name(text)
                email = extract_email(text)
                phone = extract_phone(text)
                college = extract_college(text)
                
                print("\n========== RAW RESUME TEXT ==========")
                print(text[:3000])   # first 3000 characters
                print("====================================")
                print("\n========== RESUME DETAILS ==========")
                print("Name :", name)
                print("Email :", email)
                print("Phone :", phone)
                print("College :", college)

            except Exception as e:

                print("Resume Error :", e)

        else:

            print("\nResume Not Found")

        print("\n========== RESUME DETAILS ==========")
        print("Name           :", name)
        print("Email          :", email)
        print("Phone          :", phone)
        print("College        :", college)
        print("===================================")
    

    
        # -------------------------------
        # STEP 4: AADHAAR EXTRACTION
        # -------------------------------
        aadhar_path = ""

        for ext in [".jpg", ".jpeg", ".png", ".pdf"]:

            temp = os.path.join(folder_path, "aadhar" + ext)

            if os.path.exists(temp):
                aadhar_path = temp
                break

        aadhar_name = ""

        aadhar_details = {
            "name": "",
            "year_of_birth": "",
            "gender": "",
            "aadhar_number": ""
        }

        if aadhar_path:

            aadhar_text = extract_text_from_image(
                aadhar_path
            )
            print("\nRAW AADHAAR OCR")
            print(aadhar_text)
            aadhar_details = extract_aadhar_details(
                aadhar_text
            )
            print(type(aadhar_details))
            print(aadhar_details)
            aadhar_name = aadhar_details["name"]
            

        else:

            print("\nAADHAAR NOT FOUND")
        
        #photo

        photo_path = ""

        for ext in [".jpg", ".jpeg", ".png",".pdf"]:

            temp = os.path.join(folder_path, "photo" + ext)

            if os.path.exists(temp):
                photo_path = temp
                break

        if photo_path:

            print("\nPASSPORT PHOTO FOUND")

            if photo_path.lower().endswith(".pdf"):

                print("Passport Size Photo (PDF) : Accepted")

            else:

                if verify_photo(photo_path):
                    print("Passport Size Photo : Verified")
                else:
                    print("Passport Size Photo : INVALID")
        

        # -------------------------------
        # STEP 5: COLLEGE ID EXTRACTION
        # -------------------------------
        college_name = ""

        collegeid_details = {
            "college": "",
            "reg_no": "",
            "name": ""
        }

        collegeid_path = ""

        for ext in [".jpg", ".jpeg", ".png", ".pdf"]:

            temp = os.path.join(folder_path, "collegeid" + ext)

            if os.path.exists(temp):
                collegeid_path = temp
                break

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

        offer_path = os.path.join(
            folder_path,
            "offerletter.pdf"
        )

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

            offer_details = {
                "name": "",
                "register_no": "",
                "college": "",
                "technology": "",
                "enrollment_id": "",
                "start_date": "",
                "end_date": ""
            }

        
        # -------------------------------
        # STEP 6: EMAIL BODY EXTRACTION
        # -------------------------------

        email_details = {
            "name": "",
            "register_no": "",
            "domain": "",
            "start_date": "",
            "end_date": ""
        }

        email_body_path = os.path.join(
            folder_path,
            "email_body.txt"
        )

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
        # STEP 7: DOCUMENT CHECK
        # -------------------------------

        missing_docs, invalid_docs = check_documents(folder_path)

        # -------------------------------
        # STEP 8: NAME VERIFICATION
        # -------------------------------

        result = {
            "resume_status": "MISSING",
            "aadhar_status": "MISSING",
            "college_status": "MISSING",
            "offer_status": "MISSING",
            "status": "MANUAL REVIEW",
            "score": 0
        }

        result = verify_all_names(
            master_name,
            name,
            aadhar_name,
            college_name,
            offer_details["name"]
        )

        print("\n========== FINAL VERIFICATION ==========")
        print("Resume   :", result["resume_status"])
        print("Aadhaar  :", result["aadhar_status"])
        print("College  :", result["college_status"])
        print("Offer    :", result["offer_status"])
        print("----------------------------------------")
        print("STATUS :", result["status"])
        print("SCORE  :", result["score"])
        print("========================================")

        # ----------------------------------
        # SAVE EXTRACTED DETAILS
        # ----------------------------------

        details_file = os.path.join(
            folder_path,
            "extracted_details.txt"
        )

        with open(details_file, "w", encoding="utf-8") as f:

            f.write("=" * 60 + "\n")
            f.write("AI INTERN DOCUMENT VERIFICATION\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Candidate Folder : {folder_name}\n\n")

            f.write("RESUME\n")
            f.write("------------------------------\n")
            f.write(f"Name : {name}\n")
            f.write(f"Email : {email}\n")
            f.write(f"Phone : {phone}\n")
            f.write(f"College : {college}\n\n")

            f.write("AADHAAR\n")
            f.write("------------------------------\n")
            f.write(f"Name : {aadhar_details['name']}\n")
            f.write(f"Aadhaar : {aadhar_details['aadhar_number']}\n")
            f.write(f"Gender : {aadhar_details['gender']}\n")
            f.write(f"Year : {aadhar_details['year_of_birth']}\n\n")

            f.write("COLLEGE ID\n")
            f.write("------------------------------\n")
            f.write(f"Name : {collegeid_details['name']}\n")
            f.write(f"Register No : {collegeid_details['reg_no']}\n")
            f.write(f"College : {collegeid_details['college']}\n\n")

            f.write("OFFER LETTER\n")
            f.write("------------------------------\n")
            f.write(f"Name : {offer_details['name']}\n")
            f.write(f"Enrollment ID : {offer_details['enrollment_id']}\n")
            f.write(f"Technology : {offer_details['technology']}\n")
            f.write(f"Start Date : {offer_details['start_date']}\n")
            f.write(f"End Date : {offer_details['end_date']}\n\n")

            f.write("EMAIL BODY\n")
            f.write("------------------------------\n")
            f.write(f"Name : {email_details['name']}\n")
            f.write(f"Register No : {email_details['register_no']}\n")
            f.write(f"Domain : {email_details['domain']}\n\n")

            f.write("VERIFICATION RESULT\n")
            f.write("------------------------------\n")
            f.write(f"Resume : {result['resume_status']}\n")
            f.write(f"Aadhaar : {result['aadhar_status']}\n")
            f.write(f"College : {result['college_status']}\n")
            f.write(f"Offer : {result['offer_status']}\n")
            f.write(f"Final Status : {result['status']}\n")
            f.write(f"Score : {result['score']}\n")


        uploaded_files = ", ".join(
            os.listdir(folder_path)
        )


        print("missing_docs =", missing_docs)
        print("invalid_docs =", invalid_docs)
        # -------------------------------
        # STEP 8: PREPARE PROCESSED FOLDER
        # -------------------------------

        os.makedirs("processed", exist_ok=True)

        if offer_details["name"] and offer_details["enrollment_id"]:

            safe_name = re.sub(
                r'[^A-Za-z0-9 ]',
                '',
                offer_details["name"]
            ).strip().replace(" ", "_")

            processed_folder_name = (
                f"{safe_name}_{offer_details['enrollment_id']}"
            )

        else:

            processed_folder_name = folder_name


        processed_folder = os.path.join(
            "processed",
            processed_folder_name
        )


        # -------------------------------
        # STEP 9: SAVE CSV
        # -------------------------------

        save_to_csv(

            processed_folder_name,

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

            ", ".join(missing_docs + invalid_docs),

            result["status"]

        )


        # -------------------------------
        # STEP 10: MOVE TO PROCESSED
        # -------------------------------

        if os.path.exists(processed_folder):

            shutil.rmtree(processed_folder)

        shutil.move(folder_path, processed_folder)

        print("Moved To :", processed_folder)
        
# # -------------------------------
# MAIN RUN
# -------------------------------

if __name__ == "__main__":

    # Fetch emails from Gmail
    candidates = fetch_emails()

    print("\nEMAILS DOWNLOADED")

    # If no emails found
    if len(candidates) == 0:
        print("No new emails found.")
    else:
        run_pipeline(candidates)

    print("\n==============================")
    print("PROCESS COMPLETED SUCCESSFULLY")
    print("==============================")