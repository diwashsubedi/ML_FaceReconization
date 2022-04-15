import cv2
import numpy as np
import face_recognition
import os

path = 'ImagesAttendance'
images


def mainfun():
    # Image import
    imgDiwas = face_recognition.load_image_file('ImageMain/Diwash.jpg')
    imgDiwas = cv2.cvtColor(imgDiwas, cv2.COLOR_BGR2RGB)
    imgTest = face_recognition.load_image_file('ImageMain/Bobby.jpg')
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)


if __name__ == '__main__':
    mainfun()
