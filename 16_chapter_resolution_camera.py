# RESOLUTINS OF WEBCAM

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

def hd_resolution():

    cap.set(3,1280)
    cap.set(4,720)

def sd_resolution():

    cap.set(3,640)
    cap.set(4,480)

def fhd_resolution():

    cap.set(3,1920)
    cap.set(4,1080)

# hd_resolution()
# sd_resolution()
fhd_resolution()


while(cap.isOpened()== True):

    # capture frame by frame
    ret, frame = cap.read()
    
    if ret==True:
        cv.imshow("Web1",frame)

        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break

# Step-5 Release or close the window

cap.release()
cv.destroyAllWindows()