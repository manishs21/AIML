import cv2 as cv
import numpy as np

img = cv.imread(r"images\Mountains.png")

# #resize:

# resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
# cv.imshow("image", resized)

# #Flipping
# flipped = cv.flip(img, 0) #1 for horizontal 0 for verticle -1 for both
# cv.imshow("Original image", img)
# cv.imshow("Flipped image", flipped)

# #Cropping
# cropped = img[100:500, 200:300]
# cv.imshow("Cropped image", cropped)


def translate(img, x, y):
    trans_mat = np.float32(([1, 0, x], [0, 1, y]))
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)

translated = translate(img, 200, 100)
cv.imshow("Original Image", img)
cv.imshow("Translated Image", translated)


def rotate(img, angle, rotpoint = None):
    (height, width) = img.shape[:2] # 0 --height & 1--- width
    
    if rotpoint is None:
        rotpoint = (width // 2, height // 2)
        
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotmat, dimensions)

rotated = rotate(img, 90)
cv.imshow("Rotated Image", rotated)
cv.waitKey(0)


# def rotate(img, angle, rotpoint = None):
#     (height, width) = img.shape[:2] # 0 -> height & 1 - > Widht
    
#     if rotpoint is None:
#         rotpoint = (width // 2, height // 2)
        
#     rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
#     dimesions = (width, height)
    
#     return cv.warpAffine(img, rotmat, dimesions)
#     return cv.warpAffine(img, rotmat, dimesions)

# rotated = rotate(img, 90)
# cv.imshow("Original Image", img)
# cv.imshow("Rotated Image", rotated)
# cv.waitKey(0)