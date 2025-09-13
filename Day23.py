import cv2 as cv
import numpy as np

# # Create two blank images
# img1 = np.zeros((300, 300), dtype= "uint8") # rectangle
# img2 = np.zeros((300, 300), dtype= "uint8") # circle

# # Draw a rectangle on image 1
# cv.rectangle(img1, (50,50), (250,250), 255, -1)

# # Draw a white circle on image 2
# cv.circle(img2, (150, 150), 120,255, -1)

# cv.imshow("Rectangle", img1)
# cv.imshow("Circle", img2)

# #AND operation intersection
# bit_and = cv.bitwise_and(img1, img2)
# cv.imshow("AND", bit_and)


# # Or Operation # union part
# bit_or = cv.bitwise_or(img1,img2)
# cv.imshow("Bitwise-Or",bit_or)

# # Xor Operation # except intersection part
# bit_xor = cv.bitwise_xor(img1,img2)
# cv.imshow('Bitwise-Xor',bit_xor)

# # Not operation 
# bit_not_rectangle = cv.bitwise_not(img1)
# cv.imshow("Bitwise-Not-Rectangle",bit_not_rectangle)
# bit_not_circle = cv.bitwise_not(img2)
# cv.imshow("Bitwise-Not-Circle",bit_not_circle)

# #Masking
# img = cv.imread(r"images\BL.jpg")

# resized_img = cv.resize(img, (900, 1200))

# #Create a mask
# img_mask = np.zeros(resized_img.shape[:2], dtype = "uint8")

# # Create a white circle in the mask
# cv.circle(img_mask, (350,400), 350, 255, -1)

# #Apply the mask
# masked_img = cv.bitwise_and(resized_img, resized_img, mask = img_mask)

# #Show
# cv.imshow("Original", resized_img)
# cv.imshow("Mask", img_mask)
# cv.imshow("Masked image", masked_img)


# cv.waitKey(0)
# cv.destroyAllWindows


img = cv.imread(r"images\Mountains.png")

resized_img = cv.resize(img, (900, 900))

# Splitting the channels
B, G, R = cv.split(resized_img)

# cv.imshow("Original Image", resized_img)
# cv.imshow("Gray -> blue", B)
# cv.imshow("Gray -> Green", G)
# cv.imshow("Gray -> Red", R)

merged = cv.merge([B, G, R])
cv.imshow("merged_image", merged)

zeros = np.zeros_like(B)
Blue_visual = cv.merge([B, zeros, zeros])
Green_visual = cv.merge([zeros, G, zeros])
Red_visual = cv.merge([zeros, zeros, R])

cv.imshow("Blue", Blue_visual)
cv.imshow("Green", Green_visual)
cv.imshow("Red", Red_visual)

# img_gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
# Red_visual = cv.merge([img_gray, img_gray, R])
# cv.imshow("Red", Red_visual)

cv.waitKey(0)
cv.destroyAllWindows()