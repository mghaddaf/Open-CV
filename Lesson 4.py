import cv2
minecraft = cv2.imread(r"Open CV\Images\panorama.jpg", cv2.IMREAD_COLOR)
cv2.imshow("minecraft", minecraft)
# drawing line on screen
thickness = 1 
color = 255, 191, 0
startpos = 100, 100
endpos = 100, 200
line = cv2.line(minecraft, startpos, endpos, color, thickness)
cv2.imshow("line", line)
cv2.waitKey(0)
# drawing rectangle on screen
thickness = -1
color = 200, 255, 100
startpos = 100, 100
endpos = 200, 200
rectangle = cv2.rectangle(minecraft, startpos, endpos, color, thickness)
cv2.imshow("rectangle", rectangle)
cv2.waitKey(0)