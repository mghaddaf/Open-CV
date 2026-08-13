import cv2
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
