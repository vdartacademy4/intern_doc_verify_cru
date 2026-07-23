import imaplib

EMAIL = "your_actual_email@gmail.com"
APP_PASSWORD = "your_actual_16_character_app_password"

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(EMAIL, APP_PASSWORD)
    print("✅ Login Successful")
    mail.logout()

except Exception as e:
    print("❌ Login Failed")
    print(e)