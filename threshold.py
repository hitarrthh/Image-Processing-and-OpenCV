import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# SIMPLE THRESHOLDING (MANUALLY SPECIFY THE THRESHOLD VALUE)
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
#thresh = img
#threshold = the value you passed in (125,255)
cv.imshow('THRESHOLD',thresh)

threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # Opposite of normal thresholding
cv.imshow('THRESHOLD inverse',thresh_inv)

# ADAPTIIVE THRESHOLDING (USED TO FIND OPTIMAL THRESHOLDING VALUE)
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
# img,max value,method,type,block size, c-value
cv.imshow(' adaptive THRESHOLD',adaptive_thresh)


cv.waitKey(0)