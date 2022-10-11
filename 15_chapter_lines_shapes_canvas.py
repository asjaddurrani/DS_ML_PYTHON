# HOW TO DRAW LINES AND SHAPES IN PYTHON

import cv2 as cv
import numpy as np

# Draw a canvas
black_img = np.zeros((600,600)) # 0 for Black
white_img = np.ones((600,600)) # 1 for White

# Print Size
print("Th size of our canvas is: ",black_img.shape)

# Print Image
print(black_img)

# Color the canvas
colored_img = np.zeros((600,600,3),np.uint8)  #color channel addition
colored_img[:] = 255,0,255 # Colored complete image
colored_img[150:230, 100:500] = 255,168,10  # part of image to be color

# Adding Line
cv.line(colored_img,(100,100),(300,300),(255,0,50),3) # Part line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,50),3) # Cross line

# Adding Rectangle
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),3) # Draw
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255), cv.FILLED) # Filled

# Adding Circle
cv.circle(colored_img,(400,300),50,(255,255,255),3) # Draw
cv.circle(colored_img,(400,300),50,(255,255,255), cv.FILLED) # Filled

# Adding Circle
cv.circle(colored_img,(400,300),50,(255,255,255),3) # Draw
cv.circle(colored_img,(400,300),50,(255,255,255), cv.FILLED) # Filled

# Adding Text
cv.putText(colored_img,"Python Ka Chilla",(200,500),cv.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)


# Display
# cv.imshow("Black",black_img)
# cv.imshow("White",white_img)
cv.imshow("Colored",colored_img)

cv.waitKey(0)
cv.destroyAllWindows()