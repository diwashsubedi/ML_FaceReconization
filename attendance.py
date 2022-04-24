from datetime import datetime
import time


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:  # open the file in read and write mode
        myDataList = f.readlines()  # all line in myDataList
        nameList = []
        dateList = []

        # this block will copy name and datetime in the list
        for line in myDataList:
            entry = line.split(',')
            print("Entry 0 ", entry[0])
            nameList.append(entry[0])
            if name in entry[0]:
                dateList.append(entry[1])
        dtstr = time.strftime("%m/%d/%Y")

        #  check whether the name already exist in the system or not
        if name in nameList:
            if dtstr not in dateList:
                now = datetime.now()
                tiString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtstr},{tiString}')
        if name not in nameList:
            now = datetime.now()
            tiString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstr},{tiString}')
