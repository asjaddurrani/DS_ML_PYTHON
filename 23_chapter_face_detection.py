# HOW TO DETECT FACE

# face dtection
import cv2 as cv

face_cascade = cv.CascadeClassifier('resources/file.xml')

img = cv.imread("resources/image1.jpg")

img = cv.resize(img,(400,400))

gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_scale,1.1,4)

for (x,y,w,h) in face:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow("First image",img)

cv.waitKey(0)
cv.destroyAllWindows()


# LAST LECTURE OF 40 DAYS COURSE