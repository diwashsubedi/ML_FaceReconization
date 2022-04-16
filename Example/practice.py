import cv2
import numpy as np
import face_recognition


def name_attendance():
    # Image import
    imgDiwas = face_recognition.load_image_file('../ImageMain/Diwash.jpg')
    imgDiwas = cv2.cvtColor(imgDiwas, cv2.COLOR_BGR2RGB)
    imgTest = face_recognition.load_image_file('../ImageMain/Bobby.jpg')
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

    # Face Detect
    faceLoc = face_recognition.face_locations(imgDiwas)[0]
    encodeDiwash = face_recognition.face_encodings(imgDiwas)[0]
    cv2.rectangle(imgDiwas, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

    # Face Detect
    faceLocTest = face_recognition.face_locations(imgTest)[0]
    encodetest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

    # Comparing the distance and finding the spaces
    result = face_recognition.compare_faces([encodeDiwash], encodetest)
    faceDis = face_recognition.face_distance([encodeDiwash], encodetest)
    print(result, faceDis)
    cv2.putText(imgTest, f'{result}{round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    # Image Show
    cv2.imshow('Diwash Subedi', imgDiwas)
    cv2.imshow('Diwash Test', imgTest)
    cv2.waitKey(0)


if __name__ == '__main__':
    name_attendance()
