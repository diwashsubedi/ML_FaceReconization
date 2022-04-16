from datetime import datetime
import time


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        dateList = []
        print("myDataList",myDataList)
        for line in myDataList:
            entry = line.split(',')
            print(entry)
            nameList.append(entry[0])
            dateList.append(entry[1])
        dtstr = time.strftime("%Y/%m/q%d")
        if name in nameList:
            if dtstr not in dateList:
                now = datetime.now()
                tiString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtstr},{tiString}')
            #f.writelines(f'\n{name},{dtstr}')
        if name not in nameList:
            now = datetime.now()
            tiString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstr},{tiString}')