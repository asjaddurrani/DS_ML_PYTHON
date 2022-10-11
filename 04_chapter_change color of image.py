# CHANGE IMAGE INTO BLACK AND WHITE

import cv2 as cv

img = cv.imread("resources/image.jpg")

img = cv.resize(img,(400,400))

gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# change gray scale image into black and white
(thresh,binary) = cv.threshold(gray_scale,127,255,cv.THRESH_BINARY)

cv.imshow("Orignal",img)
cv.imshow("Gray",gray_scale)
cv.imshow("black and white",binary)

cv.waitKey(0)
cv.destroyAllWindows()