import os

def check_documents(folder_path):

    required_docs = [
        "resume",
        "aadhar",
        "collegeid",
        "offerletter",
        "email_body",
        "photo"
    ]

    uploaded_files = os.listdir(folder_path)

    missing = []

    for doc in required_docs:

        found = False

        for file in uploaded_files:

            filename = os.path.splitext(file)[0].lower()

            if filename == doc:
                found = True
                break

        if not found:
            missing.append(doc)

    return missing