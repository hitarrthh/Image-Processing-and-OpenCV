import cv2 as cv
import numpy as np
blank = np.zeros((400,400),dtype='uint8')

rect = cv.rectangle(blank.copy(),(30,30),(370,370),255,cv.FILLED)
circle = cv.circle(blank.copy(),(200,200),200,255,cv.FILLED)
cv.imshow('rectangke',rect)
cv.imshow('labcircle',circle)

# AND OPERATOR: GIVES THE INTERCEPT AFTER OVERLAPPING BOTH THE IMAGES (COMMON REGIONS IN BOTH IMAGE IS RETURNED)
bitwise_and = cv.bitwise_and(rect,circle)
cv.imshow('AND OPERATOR',bitwise_and)

# OR OPERATOR: GIVES INTERSECTING AND NON-INTERSECTING REGION OF BOTH THE IMAGES
bitwise_or = cv.bitwise_or(rect,circle)
cv.imshow('OR OPERATOR',bitwise_or)

# X-OR OPERATOR: GIVES THE NON-INTERSECTING REGIONS
bitwise_xor = cv.bitwise_xor(rect,circle)
cv.imshow('XOR OPERATOR',bitwise_xor)

# NOT OPERATOR: INVERTS THE BINARY COLOUR
bitwise_not = cv.bitwise_not(rect)
cv.imshow('NOT OPERATOR',bitwise_not)

cv.waitKey(0)