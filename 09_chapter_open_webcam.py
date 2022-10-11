# HOW TO CAPTURE A WEBCAM INSIDE PYTHON

# Step-1 Import Libraries

import cv2 as cv
import numpy as np

# Step-2 Read the frame from camera

cap = cv.VideoCapture(0)  # webcam no 1

# Step-3 Display frame by frame

while(cap.isOpened()== True):

    # capture frame by frame
    ret, frame = cap.read()

    if ret==True:

        # To display frame
        cv.imshow("Webcam",frame)

        # to quit with key "q"
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    
    else:
        break

# Step-4 Release or close the window

cap.release()
cv.destroyAllWindows()