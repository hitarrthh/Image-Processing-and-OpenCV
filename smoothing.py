import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 

#IN ORDER TO BLUR THE CENTER OF THE KERNEL POIN IS BLURRED

# AVERAGING: TAKE AVERAGE OF ALL THE OTHER POINT EXCEPT THE CENTER 
average = cv.blur(img,(3,3))
cv.imshow('average blur',average)

# GAUSSIAN: GIVES DIFFERENT WEIGHTS EXCEPT THE CENTER POINT AND TAKE THE AVERAGE OF THE PRODOUVT
#  (MORE NATURAL BUT LESS EFFECTIVE COMPARED TO AVERAGING)
gaussian = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Gaussian blur',gaussian)

# MEDIAN: TAKES MEDIUM OF THE CEELS EXCEPT THE CENTER
# MORE EFFECTIVE IN REDUCING NOISE COMAPRED TO GAUSSIAN AND AVERAGING
median = cv.medianBlur(img,3)
cv.imshow('median blyr',median)

# BILATERIAL: IT RETAINS THE IMAGE (OTHER DON'T DO THAT)
# MOST EFFECTIVE
bilaterial = cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral blur',bilaterial)


cv.waitKey(0)