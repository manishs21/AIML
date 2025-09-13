import cv2 as cv
import numpy as np

img = cv.imread(r"images\BL.jpg")
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)


# lap = cv.Laplacian(gray, cv.CV_64F)  #second derivative
# lap = np.uint8(np.absolute(lap))
# cv.imshow("Laplacian", lap)


#sobel method
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("sobel - x", sobel_x)
cv.imshow("sobel - y", sobel_y)

combained_sobel = cv.bitwise_or(sobel_x, sobel_y)
combained_sobel = np.uint8(np.absolute(combained_sobel))

cv.imshow("Combained_sobel", combained_sobel)



cv.waitKey(0)
