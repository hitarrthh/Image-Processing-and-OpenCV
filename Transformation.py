import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 

#TRANSLATION (shifting image in x and y axis)
def translate(img,x,y):
    transmat = np.float32( [ [1,0,x], [0,1,y] ] )
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)
# -x = left
#-y = up
#+x = right
#+y = down
translated = translate(img,1-00,100)
cv.imshow('translate',translated)

#ROTATION 
def rotate(img,angle,point=None):
    (height,width) = img.shape[1],img.shape[0]
    if point is None:
        point  = (height//2,width//2)
    rotmat = cv.getRotationMatrix2D(point,angle,1.0)
    dim = (width,height)
    return cv.warpAffine(img,rotmat,dim)
rotated = rotate(img,90)
# Negative value for angle rotates the image in clock-wise fashion
cv.imshow('rotate',rotated)
rotated_twice = rotate(rotated,45)
cv.imshow('rotate an rotated image',rotated_twice)

#RESIZE 
resize = cv.resize(img,(500,500),interpolation = cv.INTER_CUBIC)
cv.imshow("resise",resize)

#FLIPPING
flip = cv.flip(img,-1)
# 0 = flipping vertically (over the x-axis)
# 1 = flipping horizontally (over the y-axis) (mirror image)
# -1 = both
cv.imshow('flipped',flip)

#CROPPING
crop = img[10:200,200:400]
cv.imshow('cropped',crop)

cv.waitKey(0)