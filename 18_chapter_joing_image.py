# JOINING THE IMAGE (only images with same color,height and width)

# import library
import cv2 as cv
import numpy as np

# read the image
img = cv.imread("resources/image.jpg")
img = cv.resize(img,(400,400))

#Stacking same image

# Horizontal stack
hor_img = np.hstack((img,img))

# Vertical stack
ver_img = np.vstack((img,img))


# cv.imshow("Horizontal Stack",hor_img)
cv.imshow("Vertical Stack",ver_img)


cv.waitKey(0)
cv.destroyAllWindows()