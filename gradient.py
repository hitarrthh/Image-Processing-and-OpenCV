import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray) 
# LAPLICAN
lap = cv.Laplacian(gray,cv.CV_64F) # COMPUTES GRADIENT (HAS NEHATIVE VAUE AND IMAGES CANNOT HAVE NEGATIVE VALUES)
lap = np.uint8(np.absolute(lap))
cv.imshow('LAPLICIAN',lap) 

# SOBEL 
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('SOBEL X',sobel_x) 
cv.imshow('SOBEL Y',sobel_y) 
combined = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('COMBINED COBEL',combined) 

# CANNY (MULTI-STAGE PROCESS ONE OF ITS STAGES USES SOBEL)
canny = cv.Canny(gray,150,175)
cv.imshow('CANNY',canny) 

cv.waitKey(0)