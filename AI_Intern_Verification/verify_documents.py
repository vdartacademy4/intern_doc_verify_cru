def verify_names(resume_name, aadhar_name):

    resume_name = resume_name.strip().lower()
    aadhar_name = aadhar_name.strip().lower()

    if resume_name == aadhar_name:
        return "Verified"

    return "Mismatch"