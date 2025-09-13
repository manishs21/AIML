#Blurring
import cv2 as cv

img = cv.imread(r"images\dog.webp")
resized = cv.resize(img, (600, 600))
cv.imshow("Image", resized)

# #Average Blur
# avg_blur = cv.blur(resized, (3,3))
# cv.imshow("Average Blur", avg_blur)

# # Median Bluring
# median_blur = cv.medianBlur(resized, 5) #number should be odd
# cv.imshow("Median Blur", median_blur)

# # Gaussian Blur
# Gauss_Blur = cv.GaussianBlur(resized, (5,5), 0)
# cv.imshow("Gaussian blur", Gauss_Blur)

# Bilateral Blur
bilateral = cv.bilateralFilter(resized, 15, 20, 20)
cv.imshow("Bilateral_Blur", bilateral)

cv.waitKey(0)




