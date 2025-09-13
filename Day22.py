import cv2 as cv

img = cv.imread(r"images\cat.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#simple Threshold
threshold, thres_img = cv.threshold(gray, 135, 255, cv.THRESH_BINARY)
threshold, thres_img_inv = cv.threshold(gray, 135, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold image", thres_img)
cv.imshow("Simple Threshold image", thres_img_inv)

#Adaptive Threshold
adp_thres_image = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY,
                                       10, 2)
cv.imshow("Adaptive_Threshold", adp_thres_image)


# Adaptive Threshold
adaptive_thres_img_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                          cv.THRESH_BINARY,
                                          11, 2)
cv.imshow("Adaptive_Threshold_mean", adaptive_thres_img_mean)

adaptive_thres_img_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv.THRESH_BINARY,
                                          11, 2)
cv.imshow("Adaptive_Threshold_gauss", adaptive_thres_img_gauss)



#Colour Spaces
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)


cv.imshow("HSV_IMG", hsv)
cv.imshow("HLS_IMG", hls)
cv.imshow("RGB_IMG", rgb)
cv.imshow("YCRCB_IMG", ycrcb)

cv.waitKey(0)