import cv2
minecraft = cv2.imread(r"Open CV\Images\mc banner.png", cv2.IMREAD_COLOR)
cv2.imshow("minecraft banner", minecraft)
# to convert the image to grayscale 
grayscale = cv2.cvtColor(minecraft, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale", grayscale)
cv2.waitKey(0)
# to convert the image to hsv format
minecraft = cv2.imread(r"Open CV\Images\mc banner.png", cv2.IMREAD_COLOR)
HSV = cv2.cvtColor(minecraft, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", HSV)
cv2.waitKey(0)
# to rotate the image a desired amount of degrees
minecraft = cv2.imread(r"Open CV\Images\mc banner.png", cv2.IMREAD_COLOR)
(rows, columns) = minecraft.shape[0 : 2]
matrix =  cv2.getRotationMatrix2D((columns / 2, rows / 2), 45, 1)
warped = cv2.warpAffine(minecraft, matrix, (columns, rows))
cv2.imshow("rotation", warped)
cv2.waitKey(0)