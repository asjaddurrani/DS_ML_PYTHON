# COMPARE SIZE OF TWO IMAGES

# import library
from distutils.util import convert_path
from lib2to3.pytree import convert
import cv2 as cv
from matplotlib.colors import ColorConverter
from matplotlib.pyplot import gray

# read the image
img = cv.imread("resources/image.jpg")

# give size to image
img = cv.resize(img,(400,400))

# Color Coversion
gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Display Code
cv.imshow("First image",img)
cv.imshow("Second image",gray_scale)

# Delay Code
cv.waitKey(0)
cv.destroyAllWindows()