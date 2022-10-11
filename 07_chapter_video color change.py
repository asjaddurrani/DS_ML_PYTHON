# CHANGE THE VIDEO IN BLACK AND WHITE

from ast import Break
from tkinter import Frame
import cv2 as cv
from cv2 import imread

# video reading
cap = cv.VideoCapture("resources/video.mp4")


while (True):
    (ret,frame) = cap.read()
    gray_scale = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(gray_scale,127,255,cv.THRESH_BINARY)
    if ret==True:
        cv.imshow("Video",frame)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()