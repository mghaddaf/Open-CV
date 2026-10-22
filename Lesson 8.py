import cv2
import os
import numpy as mp
haarfile = "Open CV\\haarcascade_frontalface_default.xml"
Data_Sets = "Open CV\\Data Sets"
images = []
labels = []
id = 0
names = {}
for (subdirectories, directories, files) in os.walk(Data_Sets):
    for directory in directories:
        names[id] = directory
        path = os.path.join(Data_Sets, directory)
        for file in os.listdir(path):
            path2 = os.path.join(path, file)
            label = id
            images.append(cv2.imread(path2, 0))
            labels.append(label)
        id = id + 1
(width, height) = (130, 100)
(images, labels) = [mp.array(lis) for lis in [images, labels]]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)
object = cv2.CascadeClassifier(haarfile)

webcam = cv2.VideoCapture(0)
count = 1
while True:
    IsRead, Image = webcam.read()
    Greyscaled = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    faces = object.detectMultiScale(Greyscaled, 1.3, 4)
    for face in faces:
        x, y, w, h = face
        color = 0, 0, 255
        thickness = 3
        rectangle = cv2.rectangle(Image, (x, y), (x + w, y + h), color, thickness)
        face = Greyscaled[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (130, 100))
        label, prediction_score = model.predict(face_resize)        
        text = cv2.putText(Image, "%s-%.0f"%(names[label], prediction_score), (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 2)

    cv2.imshow("Image", Image)
    key = cv2.waitKey(10)
    if key == 27:
        break
    