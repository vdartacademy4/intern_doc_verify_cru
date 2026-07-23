from ocr_processor import extract_text_from_image

text = extract_text_from_image(
    "uploads/aadhar.jpg"
)

print(text)