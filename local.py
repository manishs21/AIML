import cv2 as cv
import numpy as np

img = cv.imread(r"images\BL.jpg")
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

#laplacian -> method
lap = cv.Laplacian(gray, cv.CV_64F) #second derivative -> + ve and - ve
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian", lap)

cv.waitKey(0)