import cv2 as cv

img = cv.imread(r"images\Mountains.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred_img = cv.GaussianBlur(gray, (1,1), 0)

#canny
edges = cv.Canny(blurred_img, 100, 200)
contures_canny, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

count1 = len(contures_canny)
print(count1)


#Threshold
thres_val, thres_img = cv.threshold(blurred_img, 160, 255, cv.THRESH_BINARY)
contures_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(contures_thres)
print(count2)

#Draw the Contures
img_thres = img.copy()
img_canny = img.copy()

cv.drawContours(img_canny, contures_canny, -1, (0, 255, 0), 2)

cv.drawContours(img_thres, contures_thres, -1, (0, 0, 255), 2)

cv.imshow("Conture_Canny", img_canny)
cv.imshow("Conture_thres", img_thres)

cv.waitKey(0)
cv.destroyAllWindows