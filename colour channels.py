#SPLIT AND MERGE COLOUR CHANNELS
#LIGHTER PORTION REPRESENT HIGER DISTRIBUTION OF THAT RESPECTIVE COLOUR
import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 
blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)
cv.imshow('BLUE',b)
cv.imshow('green',g)
cv.imshow('rwd',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merger',merged)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)


cv.waitKey(0)