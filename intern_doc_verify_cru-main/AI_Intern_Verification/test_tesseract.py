import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Academytraining\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

print("Exists:", os.path.exists(pytesseract.pytesseract.tesseract_cmd))

print(
    pytesseract.get_tesseract_version()
)