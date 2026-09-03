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
minecraft = cv2.imread(r"Open CV\Images\panorama.jpg", cv2.IMREAD_COLOR)
thickness = -1
color = 200, 255, 100
startpos = 300, 200
endpos = 400, 300
rectangle = cv2.rectangle(minecraft, startpos, endpos, color, thickness)
cv2.imshow("rectangle", rectangle)
cv2.waitKey(0)
# drawing circle on screen
minecraft = cv2.imread(r"Open CV\Images\panorama.jpg", cv2.IMREAD_COLOR)
radius = 100
color = 100, 200, 255
centrepos = 200, 200
thickness = 5
circle = cv2.circle(minecraft, centrepos, radius, color, thickness)
cv2.imshow("circle", circle)
cv2.waitKey(0)
# writing text on screen
minecraft = cv2.imread(r"Open CV\Images\panorama.jpg", cv2.IMREAD_COLOR)
font = cv2.FONT_ITALIC
thickness = 3
text = "welcome to minecraft"
cornerpos = 300, 100
fontscale = 2
color = 0, 0, 250
text = cv2.putText(minecraft, text, cornerpos, font, fontscale, color, thickness)
cv2.imshow("text", text)
cv2.waitKey(0)