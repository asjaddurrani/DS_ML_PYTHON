# CONVERT WEBCAM SCREEN INTO DIFFERENT COLORS(SHADES)

# Step-1 Import Libraries

import cv2 as cv
import numpy as np

# Step-2 Read the frame from camera

cap = cv.VideoCapture(0)  # webcam no 1

# writing format, codec, video writer, object and file input
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter("resources/out_video.mp4",cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

# Step-3 Display frame by frame

while(cap.isOpened()== True):

    # capture frame by frame
    ret, frame = cap.read()
    
    # Step-4 Colors
    # gray_scale = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # (thresh,binary) = cv.threshold(gray_scale,127,255,cv.THRESH_BINARY)

    if ret==True:

        # To display frame
        cv.imshow("Web1",frame)
        # cv.imshow("Web2",gray_scale)
        # cv.imshow("Web3",binary)

        # to quit with key "q"
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    
    else:
        break

# Step-5 Release or close the window

cap.release()
out.release()
cv.destroyAllWindows()