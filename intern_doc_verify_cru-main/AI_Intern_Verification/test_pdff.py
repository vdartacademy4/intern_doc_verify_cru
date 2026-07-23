from pdf2image import convert_from_path

pdf = r"uploads\candidate_1\aadhar.pdf"

pages = convert_from_path(
    pdf,
    poppler_path=r"C:\Program Files\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)

print(len(pages))