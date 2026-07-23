import imaplib
import email
import os
import ssl
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

def fetch_emails():

    context = ssl.create_default_context()

    mail = imaplib.IMAP4_SSL(
        "imap.gmail.com",
        993,
        ssl_context=context
    )

    try:
        print("EMAIL =", os.getenv("EMAIL"))
        print("APP_PASSWORD =", os.getenv("APP_PASSWORD"))
        mail.login(
            os.getenv("EMAIL"),
            os.getenv("APP_PASSWORD")
        )
        print("✅ Gmail Login Success")
    except Exception as e:

        print("Gmail Connection Failed")
        print(e)

        return []

    mail.select("inbox")

    result, data = mail.search(None, "UNSEEN")

    print("Search Result:", result)
    print("Email IDs:", data)

    email_ids = data[0].split()

    print("Total Unseen Emails:", len(email_ids))

    candidates = []

    os.makedirs("uploads", exist_ok=True)

    for e_id in email_ids:

        result, msg_data = mail.fetch(e_id, "(RFC822)")

        msg = email.message_from_bytes(msg_data[0][1])

        sender_email = email.utils.parseaddr(msg["From"])[1]

        subject = msg["Subject"] if msg["Subject"] else ""

        folder_name = f"candidate_{e_id.decode()}"

        folder_path = os.path.join(
            "uploads",
            folder_name
        )

        os.makedirs(folder_path, exist_ok=True)

        body = ""

        for part in msg.walk():

            if (
                part.get_content_type() == "text/plain"
                and part.get_content_disposition() is None
            ):

                body = part.get_payload(
                    decode=True
                ).decode(
                    errors="ignore"
                )

                break

        with open(
            os.path.join(folder_path, "email_body.txt"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write(body)

        for part in msg.walk():

            if part.get_content_disposition() == "attachment":

                filename = part.get_filename()

                if not filename:
                    continue

                original_filename = filename

                lower = filename.lower()

                ext = os.path.splitext(filename)[1].lower()

                if "resume" in lower:
                    filename = "resume" + ext

                elif (
                    "aadhaar" in lower
                    or "aadhar" in lower
                    or "uid" in lower
                ):
                    filename = "aadhar" + ext

                elif (
                    "college" in lower
                    or "id_card" in lower
                    or "student" in lower
                ):
                    filename = "collegeid" + ext

                elif (
                    "offer" in lower
                    or "internship_offer" in lower
                ):
                    filename = "offerletter.pdf"

                elif (
                    "photo" in lower
                    or "passport" in lower
                    or "passport_photo" in lower
                ):
                    filename = "photo" + ext

                else:
                    # Keep the original filename if it doesn't match any known type
                    filename = original_filename

                filepath = os.path.join(
                    folder_path,
                    filename
                )

                with open(filepath, "wb") as f:

                    f.write(
                        part.get_payload(decode=True)
                    )

                with open(
                    os.path.join(
                        folder_path,
                        "original_filename.txt"
                    ),
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(original_filename)

        candidates.append({

            "folder_name": folder_name,

            "folder_path": folder_path,

            "sender_email": sender_email,

            "subject": subject

        })

    mail.logout()
    
    return candidates