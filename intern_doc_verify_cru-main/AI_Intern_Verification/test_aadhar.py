from PIL import Image

img = Image.open(
    "uploads/22CS101_ARUN_KUMAR/aadhar.jpg"
)

print("Size:", img.size)
print("Mode:", img.mode)