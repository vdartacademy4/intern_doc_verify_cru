import os
import cv2
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Academytraining\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

POPPLER_PATH = (
    r"C:\Program Files\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)

pdf = r"uploads\candidate_1\aadhar.pdf"

pages = convert_from_path(
    pdf,
    poppler_path=POPPLER_PATH
)

print("Pages:", len(pages))

pages[0].save("temp.png", "PNG")

img = cv2.imread("temp.png")

text = pytesseract.image_to_string(img)

print("\nOCR OUTPUT:\n")
print(text)

os.remove("temp.png")