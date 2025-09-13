import cv2 as cv

#Reading Images
img = cv.imread(r"images\Mountains.png")
# cv.imshow("Image", img)

resized = cv.resize(img,(400, 400)) #image resized
# cv.imshow("Image", resized)

# flipped = cv.flip(resized, 1)#horizontally - 0
# flipped = cv.flip(resized, 0) #vertically - 0 and -1 for both
# cv.imshow("Image", flipped)

# gray = cv.cvtColor(resized, cv.COLOR_BRG2GRAY)
# cv.imshow("Gray-Image",gray)

# edge detection
# canny -> ml model
# edges = cv.Canny(img, threshold1 = 100, threshold2 = 100)
# cv.imshow("Edges", edges)

# cv.waitKey(2000) #image will show up to 2 seconds

cv.rectangle(img, (200, 200), (400, 400), (255, 0, 255), 2) #upper left coordinate 200by 200  and bottom right cordinate 400 by 400
cv.imshow("Image", img)




cv.waitKey(0)