import cv2
import numpy as np
import face_recognition
import os
from attendance import markAttendance
from Add_Student import add_student
from student_analysis import student_analysis


# function which helps to capture
def name_attendance(images, classNames):
    # find encoding images
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert from BGR format to RGB
            encode = face_recognition.face_encodings(img)[0]  # find first encoded value of the image
            encodeList.append(encode)  # add all the first value of images into the list encodeList
        return encodeList  # return the final list

    encodeListKnown = findEncodings(images)
    cap = cv2.VideoCapture(0)  # open the webcam

    while True:
        # reading data from webcam
        success, img = cap.read()
        # image resize
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        # convert into RGB from BGR
        imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # finding the location of the faces in webcam frame
        facesCurFrame = face_recognition.face_locations(imgS)
        # finding the encoding of the webcam
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        # One by One it graph one faceLoc from facesCurfame list and encoding face of the encodesCurFrame
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            # add rectangle frame and name on the face if the camera face matches to system image
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                # y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        cv2.imshow('Webcam', img)
        ch = cv2.waitKey(1)
        if ch & 0XFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def admin():
    print("Do you like to take attendance or Add new Student\n")
    choose = int(input("Press 1 for attendance, Press 2 to add new student,\nPress 3 for student analysis,  "
                       "Press 0 for end Attendance system: "))
    if choose == 1:
        for cl in myList:
            crtImg = cv2.imread(f'{path}/{cl}')
            imges.append(crtImg)
            classNames.append(os.path.splitext(cl)[0])
        name_attendance(imges, classNames)
    elif choose == 2:
        add_student()  # call the function from the Add_Student module
    elif choose == 3:
        student_analysis()  # call the function from the student_analysis module
    else:
        print("Exit from the program")


if __name__ == '__main__':
    path = 'ImageAttendance'  # file Path
    imges = []
    classNames = []
    myList = os.listdir(path)  # list of images in that path
    print("Are you student or Professor")
    system_type = int(input("Press 1 for Student Press 2 for Professor: "))
    if system_type == 1:
        student_analysis()
    elif system_type == 2:
        admin()
    else:
        print("Wrong Input")
