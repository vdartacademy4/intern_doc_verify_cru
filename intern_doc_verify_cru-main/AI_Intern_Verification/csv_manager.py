import pandas as pd
import os
from datetime import datetime

def save_to_csv(
    candidate_id,
    candidate_name,
    resume_status,
    aadhar_status,
    college_status,
    offer_status,
    email,
    phone,
    college,
    reg_no,
    aadhar_number,
    Technology,
    enrollment_id,
    start_date,
    end_date,
    uploaded_files,
    missing_docs,
    final_status
):
    

    now = datetime.now()
    data = {
        "Folder_Name": candidate_id,
        "Processed_Date": now.strftime("%Y-%m-%d"),
        "Processed_Time": now.strftime("%I:%M %p"),
        "Candidate_Name": candidate_name,
        "Resume_Name_Status": resume_status,
        "Aadhaar_Status": aadhar_status,
        "CollegeID_Status": college_status,
        "OfferLetter_Status": offer_status,
        "Email": email,
        "Phone": phone,
        "College": college,
        "Register_Number": reg_no,
        "Aadhaar_Number": aadhar_number,
        "Technology": Technology,
        "Enrollment_ID": enrollment_id,
        "Start_Date": start_date,
        "End_Date": end_date,
        "Uploaded_Files": uploaded_files,
        "Missing_Documents": missing_docs,
        "Final_Status": final_status
        
    }

    today = datetime.now().strftime("%Y-%m-%d")

    file_path = os.path.join(
        "output",
        f"report_{today}.csv"
    )

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        # Remove existing row for this candidate
        if "Folder_Name" in df.columns:
            df = df[df["Folder_Name"] != candidate_id]

        # Add latest row
        df = pd.concat(
            [df, pd.DataFrame([data])],
            ignore_index=True
        )

    else:

        df = pd.DataFrame([data])

    df.to_csv(file_path, index=False)

    print(f"CSV Updated Successfully : {candidate_id}")