# HOW TO HANGE THE PERSPECTIVE OF IMAGE

# import library
import cv2 as cv
import numpy as np

# read the image
img = cv.imread("resources/image.jpg")
img = cv.resize(img,(400,400))

print(img.shape)

# Defining Points
point1 = np.float32([[233,196],[82,471],[522,196],[715,482]])
width = 400
height = 400
width,height= 400,400
point2 = np.float32([[0,0],[800,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(point1,point2)
out_img = cv.warpPerspective(img,matrix,(width,height))

# cv.imshow("Horizontal Stack",hor_img)
cv.imshow("original",img)
cv.imshow("Perspective",out_img)


cv.waitKey(0)
cv.destroyAllWindows()