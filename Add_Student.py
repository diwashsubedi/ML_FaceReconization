import cv2
import os


def add_student():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Add Student")
    directory = r'C:\Users\Lenovo\Documents\pythonProject\MachineLearningProject\ImageAttendance'
    os.chdir(directory)  # Change the current directory to specified directory
    print(os.listdir(directory))
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("Student", frame)
        ch = cv2.waitKey(1)
        if ch & 0XFF == ord('q'):
            break
        elif ch & 0XFF == ord(' '):
            name = input("Enter name: ")
            img_name = "{}.jpg".format(name)
            cv2.imwrite(img_name, frame)
            print("Screenshot Taken")
    cam.release()
    cv2.destroyAllWindows() 