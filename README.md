
# AI Intern Verification System

An AI-powered document verification system that automatically verifies intern applications received through Gmail.

The system downloads candidate documents from email, extracts information using OCR and PDF parsing, compares candidate details across all documents, and generates a verification report automatically.

---

# Features

✅ Automatically fetch unread emails from Gmail

✅ Download attachments

✅ Rename uploaded files automatically

✅ Extract details from

- Resume (PDF)
- Aadhaar Card
- College ID Card
- Offer Letter
- Email Body

✅ OCR using EasyOCR

✅ Verify candidate name across all documents

✅ Detect missing documents

✅ Generate CSV verification report

✅ Automatically move processed candidates

✅ Scheduler checks Gmail every 2 minutes

---

# Technologies Used

- Python
- EasyOCR
- OpenCV
- pdfplumber
- RapidFuzz
- APScheduler
- Pandas
- IMAP (Gmail)

---

# Project Structure

```
AI_Intern_Verification/

│
├── app.py
├── scheduler.py
├── email_fetcher.py
├── email_body_extractor.py
├── offerletter_extractor.py
├── collegeid_extractor.py
├── aadhar_extractor.py
├── ocr_processor.py
├── verification_engine.py
├── csv_manager.py
├── document_checker.py
├── extractor.py
│
├── uploads/
├── processed/
├── rejected/
├── output/
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI_Intern_Verification.git

cd AI_Intern_Verification
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Gmail Configuration

Open

```
email_fetcher.py
```

Update your Gmail credentials

```python
mail.login(
    "your_email@gmail.com",
    "your_app_password"
)
```

Use a Gmail App Password instead of your normal password.

---

# Required Email Format

Email Body

```
Name : John Doe

Register Number : 811223104045

Domain : Python Developer

Start Date : 01-Jul-2026

End Date : 31-Jul-2026
```

---

# Required Attachments

The candidate should attach:

- Resume
- Aadhaar Card
- College ID Card
- Offer Letter
- Passport Size Photo

The attachment filenames may vary.

The system automatically renames them internally.

Example

```
Resume.pdf

John Resume.pdf

resume_final.pdf
```

↓

Automatically renamed to

```
resume.pdf
```

---

# Running the Project

Run manually

```bash
python app.py
```

Run Scheduler

```bash
python scheduler.py
```

The scheduler checks Gmail every 2 minutes.

---

# Output

After processing,

CSV Report

```
output/report.csv
```

Processed candidates

```
processed/
```

Rejected candidates

```
rejected/
```

---

# CSV Report Columns

- Folder Name
- Candidate Name
- Resume Status
- Aadhaar Status
- College ID Status
- Offer Letter Status
- Email
- Phone
- College
- Register Number
- Aadhaar Number
- Intern Domain
- Enrollment ID
- Start Date
- End Date
- Uploaded Files
- Missing Documents
- Final Status

---

# Verification Logic

The Email Body acts as the Master Record.

The following documents are verified against the Email Body:

- Resume
- Aadhaar
- College ID
- Offer Letter

RapidFuzz is used for name similarity matching.

Possible Results

- VERIFIED
- MANUAL REVIEW
- MISMATCH

---

# Author

Churchill Francis Xavier J
