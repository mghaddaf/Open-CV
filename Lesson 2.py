import cv2
import numpy as np
destroyed_land = cv2.imread(r"Open CV\Images\DESTROYED LAND.jpg", cv2.IMREAD_COLOR)
night_sky = cv2.imread(r"Open CV\Images\NIGHT SKY.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Destroyed Land", destroyed_land)
cv2.imshow("Night Sky", night_sky)

combined_images = cv2.addWeighted(destroyed_land, 0.5, night_sky, 0.5, 1) #COMBINES THE IMAGES, WITH THE NUMBERS DECIDING THE OPACITY OF EACH
cv2.imshow("COMBINED IMAGES", combined_images)
cv2.waitKey(0)

diamond = cv2.imread(r"Open CV\Images\DIAMOND.jpg", cv2.IMREAD_COLOR)
star = cv2.imread(r"Open CV\Images\STAR.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Diamond", diamond)
cv2.imshow("Star", star)

subtracted = cv2.subtract(diamond, star) #SUBTRACTS A SHAPE OR IMAGE FROM ANOTHER IMAGE BASED ON THE PIXEL VALUES
cv2.imshow("SUBTRACED", subtracted)
cv2.waitKey(0)

night_sky = cv2.imread(r"Open CV\Images\NIGHT SKY.jpg", cv2.IMREAD_COLOR)
resized = cv2.resize(night_sky, (200, 200)) #RESIZES THE IMAGE
cv2.imshow("RESIZED", resized)
cv2.waitKey(0)

# EROSION OF AN IMAGE
minecraft_menu = cv2.imread(r"Open CV\Images\minecraft menu.png", cv2.IMREAD_COLOR)
cv2.imshow("minecraft menu", minecraft_menu)
kernel = np.ones((5, 5), np.uint8)
image = cv2.erode(minecraft_menu, kernel)
cv2.imshow("eroded image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#BORDERING AROUND THE IMAGE
minecraft_menu = cv2.imread(r"Open CV\Images\minecraft menu.png", cv2.IMREAD_COLOR)
cv2.imshow("minecraft menu", minecraft_menu)
#SOLID BORDER AROUND THE IMAGE
solidborder = cv2.copyMakeBorder(minecraft_menu, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value = 1)
cv2.imshow("solidborder", solidborder)
cv2.waitKey(0)

#REFLECTIVE BORDER
reflectiveborder = cv2.copyMakeBorder(minecraft_menu, 20, 20, 20, 20, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("reflect border", reflectiveborder)
cv2.waitKey(0)

#BLURRING
minecraft_person = cv2.imread(r"Open CV\Images\minecraft person.png", cv2.IMREAD_COLOR)
cv2.imshow("minecraft person", minecraft_person)
#gaussing blurring
gaussing_blur = cv2.GaussianBlur(minecraft_person, (11, 11), 0)
cv2.imshow("gaussing blur", gaussing_blur)
cv2.waitKey(0)

#MEDIAN BLUR
median_blur = cv2.medianBlur(minecraft_person, 5)
cv2.imshow("Median blur", median_blur)
cv2.waitKey(0)