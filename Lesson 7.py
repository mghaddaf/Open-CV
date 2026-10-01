import cv2
import numpy as mp
import os
Data_Sets = r"Open CV\Data Sets"
Person = "Ryan"
path = os.path.join(Data_Sets, Person)
if not os.path.isdir(path):
    os.mkdir(path)
webcam = cv2.VideoCapture(0)
count = 1
while count <= 30:
    IsRead, Image = webcam.read()
    Greyscaled = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", Greyscaled)
    cv2.waitKey(0)
    count = count + 1
