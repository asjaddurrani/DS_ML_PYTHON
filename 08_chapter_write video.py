# SAVE VIDEO INTO FOLDER

from ast import Break
from tkinter import Frame
import cv2 as cv
from cv2 import imread

# video reading
cap = cv.VideoCapture("resources/video.mp4")

# writing format, codec, video writer, object and file input
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter("resources/out_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height),isColor=False)

while (True):
    (ret,frame) = cap.read()
    gray_scale = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # to show in player
    if ret==True:
        cv.imshow("Video",gray_scale)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()