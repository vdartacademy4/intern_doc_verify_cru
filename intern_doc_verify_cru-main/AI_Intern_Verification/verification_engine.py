from rapidfuzz import fuzz


def verify_all_names(
    master_name,
    resume_name,
    aadhar_name,
    college_name,
    offer_name
):

    # -----------------------------
    # Clean Names
    # -----------------------------
    master_name = (master_name or "").upper().strip()
    resume_name = (resume_name or "").upper().strip()
    aadhar_name = (aadhar_name or "").upper().strip()
    college_name = (college_name or "").upper().strip()
    offer_name = (offer_name or "").upper().strip()

    scores = []

    # -----------------------------
    # Resume
    # -----------------------------
    if resume_name:
        score_resume = fuzz.partial_ratio(master_name, resume_name)
        resume_status = "MATCHED" if score_resume >= 80 else "MISMATCHED"
        scores.append(score_resume)
    else:
        score_resume = 0
        resume_status = "MISSING"

    # -----------------------------
    # Aadhaar
    # -----------------------------
    if aadhar_name:
        score_aadhar = fuzz.partial_ratio(master_name, aadhar_name)
        aadhar_status = "MATCHED" if score_aadhar >= 80 else "MISMATCHED"
        scores.append(score_aadhar)
    else:
        score_aadhar = 0
        aadhar_status = "MISSING"

    # -----------------------------
    # College ID
    # -----------------------------
    if college_name:
        score_college = fuzz.partial_ratio(master_name, college_name)
        college_status = "MATCHED" if score_college >= 80 else "MISMATCHED"
        scores.append(score_college)
    else:
        score_college = 0
        college_status = "MISSING"

    # -----------------------------
    # Offer Letter
    # -----------------------------
    if offer_name:
        score_offer = fuzz.partial_ratio(master_name, offer_name)
        offer_status = "MATCHED" if score_offer >= 80 else "MISMATCHED"
        scores.append(score_offer)
    else:
        score_offer = 0
        offer_status = "MISSING"

    # -----------------------------
    # Print Scores
    # -----------------------------
    print("\n========== NAME MATCHING ==========")
    print("Master Name  :", master_name)
    print()

    print("Resume")
    print(" Name   :", resume_name)
    print(" Score  :", score_resume)
    print(" Status :", resume_status)

    print()

    print("Aadhaar")
    print(" Name   :", aadhar_name)
    print(" Score  :", score_aadhar)
    print(" Status :", aadhar_status)

    print()

    print("College")
    print(" Name   :", college_name)
    print(" Score  :", score_college)
    print(" Status :", college_status)

    print()

    print("Offer")
    print(" Name   :", offer_name)
    print(" Score  :", score_offer)
    print(" Status :", offer_status)

    # -----------------------------
    # Average Score
    # -----------------------------
    if scores:
        avg_score = sum(scores) / len(scores)
    else:
        avg_score = 0

    # -----------------------------
    # Final Status
    # -----------------------------
    statuses = [
        resume_status,
        aadhar_status,
        college_status,
        offer_status
    ]

    matched = statuses.count("MATCHED")
    missing = statuses.count("MISSING")
    mismatched = statuses.count("MISMATCHED")

    if mismatched == 0 and missing == 0:
        final_status = "VERIFIED"

    elif matched >= 2:
        final_status = "MANUAL REVIEW"

    else:
        final_status = "MISMATCH"

    print("\n========== FINAL RESULT ==========")
    print("Resume   :", resume_status)
    print("Aadhaar  :", aadhar_status)
    print("College  :", college_status)
    print("Offer    :", offer_status)
    print("----------------------------------")
    print("Average Score :", round(avg_score, 2))
    print("Final Status  :", final_status)
    print("==================================")

    return {
        "resume_status": resume_status,
        "aadhar_status": aadhar_status,
        "college_status": college_status,
        "offer_status": offer_status,
        "status": final_status,
        "score": round(avg_score, 2)
    }