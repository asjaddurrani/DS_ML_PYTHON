# GET FRAMES OF VIDEOS

from importlib import resources
from sre_constants import SUCCESS
import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/video.mp4") 

frameNr = 0

while(True):

    success,frame = cap.read()

    if success:

        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg,",frame)
    else:
        break
    frameNr = frameNr+1

cap.release()
cv.destroyAllWindows()