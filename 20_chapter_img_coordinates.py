# COORDINATES OF AN IMAGE OR VIDEO
# BGR COLOR CODES OF AN IMAGE

from tkinter import font
import cv2 as cv
import numpy as np

# Define a function

def find_coord(event,x,y,flags,params):
    if event == cv.EVENT_FLAG_LBUTTON:
        # Left mouse click
        print(x,'',y)
        #How to define to print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x) + ','+ str(y),(x,y),font,1,(255,0,0),thickness=2)
        # show the text on image and image itself
        cv.imshow("image",img)

# for color finding

    if event == cv.EVENT_RBUTTONDOWN:
        # Left mouse click
        print(x,'',y)
        #How to define to print on the same image or window
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img,str(b) + ','+ str(g)+','+str(r),(x,y),font,1,(255,0,0),thickness=2)
        cv.imshow("image",img)

# final function to read and display

if __name__=="__main__":

    # Reading the image
    img = cv.imread("resources/image.jpg",1)
    img = cv.resize(img,(600,600))

    # Display the image
    cv.imshow("image",img)

    # setting call back function
    cv.setMouseCallback("image",find_coord)

    cv.waitKey(0)
    cv.destroyAllWindows()