from ocr_processor import extract_text_from_image
from collegeid_extractor import extract_collegeid_details

result = extract_text_from_image(
    "uploads/22CS101_ARUN_KUMAR/collegeid.jpg"
)

print("OCR Output:")
print(result)

details = extract_collegeid_details(result)

print("\nExtracted Details:")
print(details)