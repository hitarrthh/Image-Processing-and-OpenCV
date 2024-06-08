import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 
blank = np.zeros(img.shape[:2],dtype='uint8') # FOR MASKING IT IS COMPULSORY TO HAVE THE SAME DIMENSION OF BLANK IMAGE AS THE REFERENCE IMAGE
#MASKING ALLOWS TO FOCUS ON CERTIAN PART OF THE IMAGE
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,cv.FILLED)
cv.imshow('circle',circle)
rect = cv.rectangle(blank.copy(),(30,30),(330,330),255,-1)
cv.imshow('rect',rect)
mask = cv.bitwise_and(rect,circle)
cv.imshow('mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('MASKED IMAGE',masked)

cv.waitKey(0)