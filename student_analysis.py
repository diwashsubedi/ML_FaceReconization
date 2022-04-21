import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


def student_analysis():
    df_attendance = pd.read_csv("Attendance.csv")  # read attendance file
    print(df_attendance)
    names_of_student = df_attendance['Name']  # finding the name of the students
    names_of_student = list(set(names_of_student))  # removing the duplicate name
    print(names_of_student)
    name = input("Enter the name of the student")  # taking the  name from the user
    if name in names_of_student:
        image = cv2.imread("ImageAttendance/{}.jpg".format(name))  # reading the user entered name image
        width, height = 450, 550  # assigning the height and the width
        dim = (width, height)
        image_half = cv2.resize(image, dim)  # Scaling
        # cv2.imshow("Half Image", image_half)
        b, g, r = cv2.split(image_half)
        height, width, channels = image_half.shape
        new_window = np.empty([height, width * 2, 3], 'uint8')
        new_window[:, 0:width] = cv2.merge([b, g, r])
        font = cv2.FONT_HERSHEY_SIMPLEX
        df_attendance_name = df_attendance.loc[(df_attendance["Name"] == name)]
        no_of_present = len(df_attendance_name["Name"])
        no_of_present = str(no_of_present)
        print(no_of_present)
        text = "Number of present day: " + no_of_present
        print(text)
        cv2.putText(new_window, name, (width, 50), font, 1, (0, 255, 255))
        cv2.putText(new_window, text, (width, 100), font, 1, (0, 255, 255))
        cv2.imshow("Half Image", new_window)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
