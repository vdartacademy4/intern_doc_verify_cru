import os
import cv2
import pytesseract
from pdf2image import convert_from_path

# -----------------------------
# Tesseract Path
# Change this only if installed elsewhere
# -----------------------------
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Academytraining\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

os.environ["TESSDATA_PREFIX"] = (
    r"C:\Users\Academytraining\AppData\Local\Programs\Tesseract-OCR\tessdata"
)

# -----------------------------
# Poppler Path
# -----------------------------
POPPLER_PATH = (
    r"C:\Program Files\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)

# -----------------------------
# Main OCR Function
# -----------------------------
def extract_text_from_image(file_path):

    print("Reading :", file_path)

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return read_pdf(file_path)

    elif extension in [".jpg", ".jpeg", ".png"]:
        return read_image(file_path)

    else:
        print("Unsupported File Type")
        return ""


# -----------------------------
# Read Image
# -----------------------------
def read_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Unable to open image")
        return ""

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    text = pytesseract.image_to_string(
        gray,
        lang="eng"
    )

    return text


# -----------------------------
# Read PDF
# -----------------------------


POPPLER_PATH = r"C:\Program Files\Release-26.02.0-0\poppler-26.02.0\Library\bin"

def read_pdf(pdf_path):

    text = ""

    try:
        print("=" * 50)
        print("INSIDE read_pdf()")
        print("Tesseract :", pytesseract.pytesseract.tesseract_cmd)
        print("Exists :", os.path.exists(pytesseract.pytesseract.tesseract_cmd))
        print("Poppler :", POPPLER_PATH)
        print("=" * 50)
        pages = convert_from_path(
            pdf_path,
            poppler_path=POPPLER_PATH,
            dpi=300
        )

        print(f"PDF Pages : {len(pages)}")

        for i, page in enumerate(pages):

            temp = f"temp_{i}.png"

            page.save(temp, "PNG")

            img = cv2.imread(temp)

            gray = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )
            print("OCR Running...")
            page_text = pytesseract.image_to_string(gray)

            text += page_text + "\n"

            os.remove(temp)

        return text

    except Exception as e:

        print("PDF Read Error :", e)

        return ""