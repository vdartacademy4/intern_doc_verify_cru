from ocr_processor import extract_text_from_image
from aadhar_extractor import extract_aadhar_details

result = extract_text_from_image(
    "uploads/22CS101_ARUN_KUMAR/aadhar.jpg"
)

details = extract_aadhar_details(result)

print(details)