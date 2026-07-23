import cv2

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

def verify_photo(photo_path):

    image = cv2.imread(photo_path)

    if image is None:
        print("Cannot read image")
        return False

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    print("Faces Detected:", len(faces))

    return len(faces) == 1