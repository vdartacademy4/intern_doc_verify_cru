# AI Intern Verification System

An AI-powered document verification system that automates the verification of internship applications received through Gmail.

The system downloads candidate documents from email, validates the uploaded files, extracts information using OCR and PDF parsing, compares candidate details across all submitted documents, generates verification reports, and stores the processed applications automatically.

---

# Features

## Email Automation

- Automatically fetch unread emails from Gmail
- Download email attachments
- Extract email body information
- Automatically rename uploaded files into standard names

---

## Document Verification

The system verifies the following documents:

- Resume (PDF)
- Aadhaar Card (PDF/Image)
- College ID Card (PDF/Image)
- Offer Letter (PDF)
- Passport Size Photo (JPG/PNG)

---

## Information Extraction

Automatically extracts:

### Resume
- Candidate Name
- Email ID
- Phone Number
- College Name

### Aadhaar
- Candidate Name
- Aadhaar Number
- Gender
- Date of Birth

### College ID
- Student Name
- Register Number
- College Name

### Offer Letter
- Candidate Name
- Enrollment ID
- Technology / Domain
- Start Date
- End Date

### Email Body
- Candidate Name
- Register Number
- Domain
- Internship Start Date
- Internship End Date

---

## Verification

- Uses Email Body as the Master Record
- Verifies candidate names across:
  - Resume
  - Aadhaar
  - College ID
  - Offer Letter
- Calculates similarity using RapidFuzz
- Detects:
  - Missing Documents
  - Invalid Documents
  - Name Mismatches

---

## Report Generation

Automatically generates:

- CSV Report
- Extracted Details Report
- Verification Result
- Processed Candidate Folder

---

## Folder Management

After successful verification:

- Moves verified candidates into the `processed` folder
- Stores extracted candidate details
- Maintains verification reports

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
- Regex
- Tesseract OCR
- Poppler

---

# Project Structure

```text
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
├── extractor.py
├── csv_manager.py
├── document_checker.py
├── folder_manager.py
├── mailer.py
│
├── uploads/
├── processed/
├── rejected/
├── output/
│
├── requirements.txt
├── README.md
└── .env
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

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file.

```env
EMAIL=your_email@gmail.com
APP_PASSWORD=your_google_app_password
```

Enable:

- Gmail IMAP
- Google 2-Step Verification
- Gmail App Password

---

# Required Email Format

Email Subject

```text
Internship Documents
```

Email Body

```text
Name : John Doe

Register Number : 811223104045

Domain : Data Analytics

Start Date : 28/04/2026

End Date : 28/07/2026
```

---

# Required Attachments

Candidate must upload:

- Resume
- Aadhaar Card
- College ID Card
- Offer Letter
- Passport Size Photo

Attachment names can be anything.

Example

```text
Resume_Final.pdf
```

↓

Automatically renamed to

```text
resume.pdf
```

---

# Running the Project

Run Once

```bash
python app.py
```

Run Scheduler

```bash
python scheduler.py
```

The scheduler checks Gmail every **2 minutes**.

---

# Generated Output

## CSV Report

```text
output/report.csv
```

## Extracted Details

```text
processed/<Candidate_Name>/extracted_details.txt
```

## Processed Candidates

```text
processed/
```

## Rejected Candidates

```text
rejected/
```

---

# CSV Report Fields

- Candidate Folder
- Candidate Name
- Resume Verification Status
- Aadhaar Verification Status
- College ID Verification Status
- Offer Letter Verification Status
- Email
- Phone Number
- College Name
- Register Number
- Aadhaar Number
- Internship Domain
- Enrollment ID
- Internship Start Date
- Internship End Date
- Uploaded Documents
- Missing Documents
- Invalid Documents
- Final Verification Status

---

# Verification Workflow

```text
Gmail
   │
   ▼
Download Email
   │
   ▼
Download Attachments
   │
   ▼
Rename Files
   │
   ▼
Document Validation
   │
   ├── Resume Extraction
   ├── Aadhaar OCR
   ├── College ID OCR
   ├── Offer Letter Extraction
   └── Email Body Extraction
   │
   ▼
Name Verification (RapidFuzz)
   │
   ▼
Generate Report
   │
   ▼
Save CSV
   │
   ▼
Generate extracted_details.txt
   │
   ▼
Move Candidate to processed/
```

---

# Verification Status

Possible Results

- VERIFIED
- MANUAL REVIEW
- MISMATCH

---

# Future Enhancements

- Face Verification using DeepFace
- Aadhaar QR Code Verification
- Streamlit Dashboard
- Email Notification for Verification Result
- Duplicate Candidate Detection
- AI-based Signature Verification

---

# Author

** Devendran A  A1593
   
   Teammate: Amrit NR

Project Developed for AI Internship Document Verification using OCR and Intelligent Document Processing.