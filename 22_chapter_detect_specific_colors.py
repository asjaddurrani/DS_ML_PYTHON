# HOW TO DETECT SPECIFIC COLORS INSIDE PYTHONS

# import libraries
import cv2 as cv
from cv2 import imread
import numpy as np

# Sliders
def slider():
    pass
path = "resources/image.jpg"
cv.namedWindow("bars")
cv.resizeWindow("bars",900,300)
cv.createTrackbar("hue min","bars",0,179,slider)
cv.createTrackbar("hue max","bars",0,179,slider)
cv.createTrackbar("sat min","bars",0,255,slider)
cv.createTrackbar("sat max","bars",255,255,slider)
cv.createTrackbar("val min","bars",0,255,slider)
cv.createTrackbar("val max","bars",255,255,slider)


while True:
    img = cv.imread(path)
    hsv_img =  cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("hue min","bars")
    hue_max = cv.getTrackbarPos("hue max","bars")
    sat_min = cv.getTrackbarPos("sat min","bars")
    sat_max = cv.getTrackbarPos("sat max","bars")
    val_min = cv.getTrackbarPos("val min","bars")
    val_max = cv.getTrackbarPos("val max","bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    # To see changes inside the window

    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])

    mask_img = cv.inRange(hsv_img,lower,upper)
    out_img = cv.bitwise_and(img,img,mask=mask_img)

    # output
    # cv.imshow('Original',img)
    # cv.imshow('HSV',hsv_img)
    cv.imshow('Mask',mask_img)
    cv.imshow('Final Output',out_img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

