# Reading Image and Displaying it

# import library
import cv2 as cv

# read the image
img = cv.imread("resources/image.jpg")

# show the image
cv.imshow("First image",img)

# image display time if 0 then its permanetly showed.
cv.waitKey(0)

# stop the output after one iteration
cv.destroyAllWindows()