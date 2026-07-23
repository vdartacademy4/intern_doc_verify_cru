from ocr_processor import extract_text_from_pdf

text = extract_text_from_pdf(
    "uploads/aadhar.pdf"
)

print(text)