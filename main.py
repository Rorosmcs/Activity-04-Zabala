import cv2 
filepath = 'robs.jpg'
imgFlag = int(1)
img = cv2.imread(filepath,imgFlag)
cv2.imshow("ZABALA", img)
cv2.waitKey(0)
cv2.destroyAllWindows()