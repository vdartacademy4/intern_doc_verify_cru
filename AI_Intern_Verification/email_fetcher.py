import imaplib
import email
import os
import time
import ssl


def fetch_emails():

    context = ssl.create_default_context()

    mail = imaplib.IMAP4_SSL(
        "imap.gmail.com",
        993,
        ssl_context=context
    )

    try:

        mail.login(
            "MAIL ID",
            "APP PASSWORD"
        )

    except Exception as e:

        print("Gmail Connection Failed")
        print(e)

        return []
    

    mail.select("inbox")

    result, data = mail.search(None, 'UNSEEN')

    email_ids = data[0].split()

    attachments = []

    for e_id in email_ids:

        result, msg_data = mail.fetch(e_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        body = ""

        for part in msg.walk():

            if part.get_content_type() == "text/plain":

                body = part.get_payload(decode=True).decode(
                    errors="ignore"
                )

                break

        # Create unique folder for this email
        folder_name = f"candidate_{e_id.decode()}"

        folder_path = os.path.join(
            "uploads",
            folder_name
        )

        os.makedirs(folder_path, exist_ok=True)

        with open(
            os.path.join(folder_path, "email_body.txt"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write(body)

        for part in msg.walk():

            if part.get_content_disposition() == "attachment":

                filename = part.get_filename()

                original_filename = filename

                lower_name = filename.lower()


                ext = os.path.splitext(filename)[1].lower()

                if "resume" in lower_name:

                    filename = "resume" + ext

                elif "aadhar" in lower_name or "aadhaar" in lower_name:

                    filename = "aadhar" + ext

                elif "college" in lower_name:

                    filename = "collegeid" + ext

                elif "photo" in lower_name:

                    filename = "photo" + ext

                # Any remaining PDF is treated as the Offer Letter
                elif ext == ".pdf":

                    filename = "offerletter.pdf"

                filepath = os.path.join(
                    folder_path,
                    filename
                )

                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))

                with open(
                    os.path.join(folder_path, "original_filename.txt"),
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(original_filename)

                attachments.append(filepath)

    return attachments
