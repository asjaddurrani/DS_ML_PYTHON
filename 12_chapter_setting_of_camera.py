# SETTING OF CAMERA(HEIGHT AND WIDTH)

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) 

# Set brightness of webcam
cap.set(10,100)  # 10 is the key for brightness

# Set hight and width
cap.set(3,640) # width key 3
cap.set(4,480) # height key 4

while(cap.isOpened()== True):

    ret, frame = cap.read()

    if ret==True:

        cv.imshow("Webcam",frame)

        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    
    else:
        break

cap.release()
cv.destroyAllWindows()