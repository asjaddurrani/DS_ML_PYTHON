# WRITE AN IMAGE OR SAVE AN IMAGE
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite

img = cv.imread("resources/image.jpg")

gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

(thresh,binary) = cv.threshold(gray_scale,127,255,cv.THRESH_BINARY)

# # Write an image
imwrite('gray_image.jpg',gray_scale)
imwrite('bw_image.jpg',binary)

cv.waitKey(0)
cv.destroyAllWindows()