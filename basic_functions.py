import cv2 as cv
img = cv.imread('PHOTOS/messi.jpg') 
cv.imshow('messi',img) 

#CONVERT IMAGE INTO GRID SCALE
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #convert image into gray color
cv.imshow('gray',gray)

#BLURRING AN IMAGE
blur = cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT) # keep the number odd in the tuple
cv.imshow('blur',blur)

#EDGE CASCADE
canny = cv.Canny(blur,175,125) #used to find the edges
#we can apply blur to reduce the edges
cv.imshow('canny',canny)

#DIALATE AN IMAGE
dialted = cv.dilate(canny,(11,11),iterations=3)
cv.imshow('dilate',dialted)

#ERODING (converting dialted image to canny)
eroded = cv.erode(dialted,(11,11),iterations=3)
cv.imshow('eroded',eroded)

#RESIZE 
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) #INTER_CUBIC gives better quality image but slower
cv.imshow('resize',resized)

#CROPPING
crop = img[30:200,200:400]
cv.imshow('crop',crop)

cv.waitKey(0)