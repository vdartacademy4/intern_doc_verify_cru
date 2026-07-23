import os
import cv2
import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):

    print("Reading:", image_path)

    if not os.path.exists(image_path):
        print("File not found:", image_path)
        return []

    img = cv2.imread(image_path)

    if img is None:
        print("OpenCV could not read:", image_path)
        return []

    result = reader.readtext(
        img,
        detail=0
    )

    return result





# import cv2
# import easyocr

# reader = easyocr.Reader(['en'])


# def extract_text_from_image(image_path):

#     # Read image
#     img = cv2.imread(image_path)

#     # Convert to grayscale
#     gray = cv2.cvtColor(
#         img,
#         cv2.COLOR_BGR2GRAY
#     )

#     # Remove noise
#     gray = cv2.GaussianBlur(
#         gray,
#         (3, 3),
#         0
#     )

#     # Increase contrast
#     gray = cv2.equalizeHist(gray)

#     # Binary Threshold
#     _, thresh = cv2.threshold(
#         gray,
#         0,
#         255,
#         cv2.THRESH_BINARY + cv2.THRESH_OTSU
#     )

#     # OCR
#     result = reader.readtext(
#         thresh,
#         detail=0,
#         paragraph=False
#     )

#     return result


# import pdfplumber
# import easyocr
# import cv2

# reader = easyocr.Reader(['en'])

# def extract_text_from_pdf(pdf_path):

#     text = ""

#     with pdfplumber.open(pdf_path) as pdf:

#         for page in pdf.pages:

#             page_text = page.extract_text()

#             if page_text:
#                 text += page_text + "\n"

#     return text


# def extract_text_from_image(image_path):

#     img = cv2.imread(image_path)

#     result = reader.readtext(
#         img,
#         detail=0
#     )

#     return result