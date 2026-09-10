import cv2
import os
from PIL import Image
path = r"Open CV\Images\mc images for lesson 5"
os.chdir(path)

totalw = 0
totalh = 0
totalimages = 0
averageh = 0
averagew = 0

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = Image.open(file)
        width, height = image.size
        totalw = totalw + width
        totalh = totalh + height
        totalimages = totalimages + 1 

averageh = totalh // totalimages
averagew = totalw // totalimages

print(averageh)
print(averagew)
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = Image.open(file)
        resized = image.resize((averagew, averageh), Image.Resampling.LANCZOS)
        resized.save(file, "JPEG", quality = 95)
video_name = "Minecraft.avi"
images = []
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = cv2.imread(file, cv2.IMREAD_COLOR)
        images.append(image)
video = cv2.VideoWriter(video_name, 0, 1, (averagew, averageh))

for image in images:
    video.write(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
video.release()
print("done")