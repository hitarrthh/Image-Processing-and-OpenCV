import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('PHOTOS/messi.jpg') 
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('messi',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
circle = cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
#GRAYSCALE HISTOGRAM
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
#image, channels, mask, bins, pixel range
cv.imshow('mask',mask)
plt.figure()
plt.plot(gray_hist)
plt.xlabel('bims ( pixel intensity)')
plt.ylabel('number of pixels')
plt.title('Gray scale histogram')
plt.show()

# COLOUR HISTOGRAM
colours = ('b','g','r')
for i,col in enumerate(colours):
    hist = cv.calcHist(img,[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.title("BGR HIstogram")
plt.show()

cv.waitKey(0)