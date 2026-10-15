import cv2
import numpy as mp
import os
haarfile = "Open CV\\haarcascade_frontalface_default.xml"
Data_Sets = r"Open CV\Data Sets"
Person = "Ryan"
print(cv2.__version__)
facecascade = cv2.CascadeClassifier(haarfile)
print(hasattr(cv2, 'CascadeClassifier'))
path = os.path.join(Data_Sets, Person)
if not os.path.isdir(path):
    os.mkdir(path)
webcam = cv2.VideoCapture(0)
count = 1
while count <= 30:
    IsRead, Image = webcam.read()
    Greyscaled = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(Greyscaled, 1.3, 4)
    for face in faces:
        x, y, w, h = face
        color = 0, 0, 255
        thickness = 3
        rectangle = cv2.rectangle(Image, (x, y), (x + w, y + h), color, thickness)
        face = Greyscaled[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (130, 100))
        cv2.imwrite("%s/%s.png"%(path, count), face_resize)
    count = count + 1
    cv2.imshow("Image", Greyscaled)
    key = cv2.waitKey(10)
    if key == 27:
        break