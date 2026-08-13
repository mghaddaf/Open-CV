import cv2
minecraft = cv2.imread(r"Open CV\Images\open cv picture.png",cv2.IMREAD_GRAYSCALE) #READS THE IMAGE, IF ITS IN COLOR OR GRAYSCALE, "UNCHANGED" MEANS THE IMAGE IS NOT CHANGED WHETHER IT IS IN COLOR OR GRAYSCALE INITIALLY
cv2.imshow("Minecraft Grass Block", minecraft) #SHOWS THE IMAGE, VARIABLE TO REPRESENT IT
cv2.waitKey(0) #WAITS UNTIL A KEY IS PRESSED THEN CLOSES THE IMAGE / WINDOW

minecraft = cv2.imread(r"Open CV\Images\open cv picture.png",cv2.IMREAD_GRAYSCALE) 
cv2.imwrite("Minecraft Grass Block.png", minecraft) #SAVES THE OUTPUT WHEN THE CODE IS RUN

minecraft = cv2.imread(r"Open CV\Images\open cv picture.png",cv2.IMREAD_COLOR)
B,G,R = cv2.split(minecraft) #SEPARATES THE COLORS INTO RED GREEN AND BLUE SECTIONS AND PUTS THEM INTO BLUE GREEN AND RED VARIABLES RESPECTIVELY
cv2.imshow("Minecraft Blue", B)
cv2.imshow("Minecraft Green", G)
cv2.imshow("Minecraft Red", R) #SPLITS THE COLORS OF THE IMAGE
cv2.waitKey(0)
