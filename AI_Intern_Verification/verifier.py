def verify_name(form_name, resume_name):

    if form_name.strip().lower() == resume_name.strip().lower():
        return "Verified"

    return "Mismatch"

def verify_college(form_college, resume_college):

    if form_college.lower() in resume_college.lower():
        return "Verified"

    return "Mismatch"