import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

#counturs = the line or curves that join the continous points along the boundary of an object
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)
counturs,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) 
# RETR_LIST = All contours
# CHAIN_APPROX_NONE = Approximation method
print('"TOTAL CONTOURS (USING CANNY)',len(counturs))

#Alternate method
ret,threshold = cv.threshold(gray,123,255,cv.THRESH_BINARY)
#Intensityon image below 125 then set to zero (black)
#Intensity of image above 255 then set to one (white)
cv.imshow('threshold',threshold)
counturs,hierarchies = cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) 
print('"TOTAL CONTOURS (USING THRESHOLD)',len(counturs))
cv.drawContours(blank,counturs,-1,(0,0,255),1)
cv.imshow('Contours drawn',blank)

cv.waitKey(0)