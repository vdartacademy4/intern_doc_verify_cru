from rapidfuzz import fuzz


def verify_all_names(
    master_name,
    resume_name,
    aadhar_name,
    college_name,
    offer_name
):
    
    master_name = (master_name or "").upper().strip()
    resume_name = (resume_name or "").upper().strip()
    aadhar_name = (aadhar_name or "").upper().strip()
    college_name = (college_name or "").upper().strip()
    offer_name = (offer_name or "").upper().strip()


    # Resume check
    score0 = fuzz.partial_ratio(
        master_name,
        resume_name 
)

    # Aadhaar check
    score1 = fuzz.partial_ratio(
        master_name,
        aadhar_name
    )

    # College ID check
    score2 = fuzz.partial_ratio(
        master_name,
        college_name
    )


    # Offer Letter check    
    score4 = fuzz.partial_ratio(
        master_name,
        offer_name
    )


    print("Master vs Resume :", score0)
    print("Master vs Aadhaar :", score1)
    print("Master vs College :", score2)
    print("Master vs Offer :", score4)

    resume_status = "MATCHED" if score0 >= 80 else "MISMATCHED"
    aadhar_status = "MATCHED" if score1 >= 80 else "MISMATCHED"
    college_status = "MATCHED" if score2 >= 80 else "MISMATCHED"
    offer_status = "MATCHED" if score4 >= 80 else "MISMATCHED"

    print("Resume :", score0, resume_status)
    print("Aadhaar :", score1, aadhar_status)
    print("College :", score2, college_status)
    print("Offer :", score4, offer_status)

    avg_score = (score0 + score1 + score2 + score4) / 4

    if resume_status == "MATCHED" and \
        aadhar_status == "MATCHED" and \
        college_status == "MATCHED" and \
        offer_status == "MATCHED":

        final_status = "VERIFIED"

    elif avg_score >= 60:

        final_status = "MANUAL REVIEW"

    else:

        final_status = "MISMATCH"

    return {
        "resume_status": resume_status,
        "aadhar_status": aadhar_status,
        "college_status": college_status,
        "offer_status": offer_status,
        "status": final_status,
        "score": round(avg_score, 2)
    }