# RESIZE THE IMAGE

# import library
import cv2 as cv

# read the image
img = cv.imread("resources/image.jpg")

# give size to image
img = cv.resize(img,(400,400))

# show the image
cv.imshow("First image",img)

# image display time if 0 then its permanetly showed.
cv.waitKey(0)

# stop the output after one iteration
cv.destroyAllWindows()

# --------------------------------------------------


# # COMPARE SIZE OF TWO IMAGES

# # import library
# import cv2 as cv

# # read the image
# img = cv.imread("resources/image.jpg")

# # give size to image
# img1 = cv.resize(img,(400,400))

# # Display Code
# cv.imshow("First image",img)
# cv.imshow("Second image",img1)

# # Delay Code
# cv.waitKey(0)
# cv.destroyAllWindows()