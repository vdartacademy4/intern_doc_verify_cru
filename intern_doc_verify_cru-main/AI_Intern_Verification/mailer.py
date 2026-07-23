import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import os

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")

PASSWORD = os.getenv("APP_PASSWORD")

def send_missing_document_mail(receiver, missing_files):

    body = f"""

Hello,

We received your internship documents.

The following files are missing.

{chr(10).join(missing_files)}

Please resend them.

Thank You.

"""

    msg = MIMEMultipart()

    msg["From"] = EMAIL

    msg["To"] = receiver

    msg["Subject"] = "Missing Internship Documents"

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(EMAIL,PASSWORD)

    server.sendmail(EMAIL,receiver,msg.as_string())

    server.quit()