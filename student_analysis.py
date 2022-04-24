import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


# this function will display the group analysis of the attendance file
def group_analysis(df_all):
    df_all.insert(len(df_all.columns), 'Present', 1)
    df = df_all[['Name', 'Present']]
    df = df.groupby(df.columns.tolist(), as_index=False).size()
    print(df)
    plt.figure(figsize=(13, 5))
    # plt.subplot(131)
    # plt.bar(df['Name'], df['size'])
    plt.xticks(rotation=16)
    # plt.subplot(132)
    plt.scatter(df['Name'], df['size'])
    # plt.xticks(rotation=16)
    # plt.subplot(132)
    # plt.xticks(rotation=16)
    # plt.plot(df['Name'], df['size'])
    # plt.suptitle("Class Attendance")
    plt.title("Class Attendance")
    plt.show()

    # second analysis
    plt.figure(figsize=(10, 7))
    daily_attendance = df_all[['Date', 'Present']]
    print("df_all", daily_attendance)
    daily_attendance = daily_attendance.groupby(daily_attendance.columns.tolist(), as_index=False).size()
    print(daily_attendance)
    plt.xticks(rotation=20)
    plt.xlabel("Date")
    plt.ylabel("No. of students")
    plt.title("Total number of students presents")
    plt.plot(daily_attendance['Date'], daily_attendance['size'])
    plt.show()


# this function will display the 3 subplot of the admin entered name
def draw_graph(name, df):
    df.insert(len(df.columns), 'Present', 1)
    df = df.set_index(df['Date'])
    print(type(df['Date']))
    print(df)
    daily_attendance = df.Present.resample('D').asfreq().fillna(0)
    print("daily_attendance", daily_attendance)
    plt.xticks(rotation=20)
    plt.plot(daily_attendance)
    plt.savefig('Student_Analysis/{}.jpg'.format(name))
    # plt.show()
    # print(df)


def student_analysis():
    df_attendance = pd.read_csv("Attendance.csv", parse_dates=['Date'])  # read attendance file
    print(df_attendance)
    names_of_student = df_attendance['Name']  # finding the name of the students
    names_of_student = list(set(names_of_student))  # removing the duplicate name
    print(names_of_student)

    print("Do you want Single student Analysis or Group analysis")
    name = input("Press 1 for Group analysis or Enter Name: ").upper()
    if name == '1':  # call the function for group analysis
        group_analysis(df_attendance)

    elif name in df_attendance["Name"].values:
        # name = input("Enter the name of the student: ")  # taking the  name from the user
        df_attendance_name = df_attendance.loc[(df_attendance["Name"] == name)]  # take only that row which matches
        # input name with system name
        draw_graph(name, df_attendance_name)  # call function to display the single person analysis

        # create the single person analysis
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
            no_of_present = len(df_attendance_name["Name"])
            no_of_present = str(no_of_present)
            print(no_of_present)
            text = "Number of present day: " + no_of_present
            print(text)
            cv2.putText(new_window, name, (width, 50), font, 1, (0, 255, 255))
            cv2.putText(new_window, text, (width, 100), font, 1, (0, 255, 255))

            # Read second image
            second_image = cv2.imread("Student_Analysis/{}.jpg".format(name))
            second_dim = 450, 400
            add_image = cv2.resize(second_image, second_dim)
            b, g, r = cv2.split(add_image)
            new_window[150:, width:width * 2] = cv2.merge([b, g, r])

            # Display
            cv2.imshow("{} Detail".format(name), new_window)

            # Save image
            cv2.imwrite('Student_Analysis_Figure/{}.jpg'.format(name), new_window)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("Entered wrong input")
