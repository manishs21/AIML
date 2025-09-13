import cv2 as cv

#Read the image
img = cv.imread(r"images\Mountains.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Haar cascade


face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 7)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("FACES", img)
cv.waitKey(0)