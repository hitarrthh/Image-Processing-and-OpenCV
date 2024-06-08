import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img)  # displays BGR image

#BGR TO GRAY SPACE
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR TO HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR TO LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR TO RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
plt.imshow(rgb) 
plt.show()

#HSV SCALE TO BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv_bgr)

#LAB TO BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab to bgr',lab_bgr)


cv.waitKey(0)
plt.imshow(img) # displays RGB image
plt.show()
