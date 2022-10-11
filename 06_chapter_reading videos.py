# READING THE VIDEO

from ast import Break
from tkinter import Frame
import cv2 as cv
from cv2 import imread

# video reading
cap = cv.VideoCapture("resources/video.mp4")

if (cap.isOpened() == False):
    print("Error")

# Rading and Playing Video

while(cap.isOpened()== True):
    ret, frame = cap.read()
    if ret==True:
        cv.imshow("Video",frame)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    
    else:
        break

cap.release()
cv.destroyAllWindows()