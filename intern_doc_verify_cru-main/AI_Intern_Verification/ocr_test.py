import easyocr
import cv2

img = cv2.imread(
    "uploads/22CS101_ARUN_KUMAR/aadhar.jpg"
)

print("Shape:", img.shape)

reader = easyocr.Reader(['en'])

result = reader.readtext(
    img,
    detail=0
)

print(result)