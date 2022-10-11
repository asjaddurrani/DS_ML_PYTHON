# HOW TO CHECK HEIGHT AND WIDTH ACTUAL AND RE-SIZE IMAGE
import cv2 as cv
import numpy as np

img = cv.imread("resources/image.jpg")
img = cv.resize(img,(600,600))

print(img.shape)

cv.waitKey(0)
cv.destroyAllWindows()