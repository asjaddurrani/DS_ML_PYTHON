# BASIC FUNCTIONS IN OPEN CV
import cv2 as cv
import numpy as np

img = cv.imread("resources/image.jpg")
img = cv.resize(img,(600,600))

# Basic Functions

# 1. Resize Image
resized_img = cv.resize(img,(300,300))

# 2. Gray Image
gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 3. Black and White
(thresh,binary) = cv.threshold(gray_scale,127,255,cv.THRESH_BINARY)

# 4. Blur image
blur_img = cv.GaussianBlur(img,(23,23),0) # kernal size(23,23) is intensity of blur and is always odd

# 5. Edge Detection
edge_img = cv.Canny(img, 48,48)

# 6. Thickness Of Lines
mat_kernal = np.ones((3,3), np.uint8)  #matices
dilated_img = cv.dilate(edge_img, (mat_kernal), iterations=1)

# 7.Thinner Lines
ero_img = cv.erode(dilated_img,mat_kernal,iterations=1)

# 7.Cropping of image
cropped_img = img[0:400 , 0:300]   # x-axis = 0:400 and y-axis = 0:300


cv.imshow("Original image",img)
cv.imshow("Gray image",gray_scale)
cv.imshow("BW image",binary)
cv.imshow("Blur image",blur_img)
cv.imshow("Edge image",edge_img)
cv.imshow("Dilate image",dilated_img)
cv.imshow("Erossion image",ero_img)
cv.imshow("Cropped image",cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()