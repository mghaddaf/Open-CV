import cv2
import os
import numpy as mp
haarfile = "Open CV\\cars (1).xml"
images = []
labels = []
id = 0
names = {}
file = cv2.VideoCapture("Open CV\\Cars.mp4")
object = cv2.CascadeClassifier(haarfile)

while file.isOpened():
    return_value, image = file.read()
    if return_value == False:
        break
    greyscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cars = object.detectMultiScale(greyscaled, 1.1, 3)
    for car in cars:
        x, y, w, h = car
        color = 0, 0, 255
        thickness = 5
        rectangle = cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)


    cv2.imshow("Image", image)
    key = cv2.waitKey(10)
    if key == 27:
        break