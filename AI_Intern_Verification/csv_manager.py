import pandas as pd
import os


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
    intern_domain,
    enrollment_id,
    start_date,
    end_date,
    uploaded_files,
    missing_docs,
    final_status
):

    data = {

    "Folder_Name": candidate_id,

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

    "Intern_Domain": intern_domain,

    "Enrollment_ID": enrollment_id,

    "Start_Date": start_date,

    "End_Date": end_date,

    "Uploaded_Files": uploaded_files,

    "Missing_Documents": missing_docs,

    "Final_Status": final_status
}

    file_path = "output/report.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        df = pd.concat(
            [df, pd.DataFrame([data])],
            ignore_index=True
        )

    else:

        df = pd.DataFrame([data])

    df.to_csv(file_path, index=False)

    print("CSV Saved Successfully")