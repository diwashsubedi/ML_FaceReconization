import cv2
import os


def add_student():
    cam = cv2.VideoCapture(0)  # open camera
    cv2.namedWindow("Add Student")  # window name
    directory = r'C:\Users\Lenovo\Documents\pythonProject\MachineLearningProject\ImageAttendance'  # directory location
    os.chdir(directory)  # Change the current directory to specified directory
    print(os.listdir(directory))
    while True:
        ret, frame = cam.read()  # reading from the camera
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("Student", frame)
        ch = cv2.waitKey(1)
        # this block is to close the camera
        if ch & 0XFF == ord('q'):  # if q is pressed by admin
            break
        # this block is to take picture
        elif ch & 0XFF == ord(' '):  # if space is pressed by user
            name = input("Enter name: ")
            img_name = "{}.jpg".format(name)
            cv2.imwrite(img_name, frame)
            print("Screenshot Taken")
    cam.release()
    cv2.destroyAllWindows()
