import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') #create a blank image uint8 = datatype for image width,height,colour(how many)
cv.imshow('blank',blank)
img = cv.imread('PHOTOS/messi.jpg')
#PAINT
blank[:] = 0,255,0 # blank image is converted into green
cv.imshow('green',blank)

blank[200:300,300:400] = 0,0,255
cv.imshow('red',blank)


#DRAW A RECTANGLE
cv.rectangle(blank , (0,0),(250,250),(255,0,0),thickness=cv.FILLED)# staring point,ending point,colour,thickness(if integer is given then it fills the border)
cv.imshow('rectangle',blank)


#DRAW A CIRCLE
cv.circle(blank,(blank.shape[1]//2 , blank.shape[0]//2),40,(0,0,255),thickness=3)# center(in the parameters it shows the way to find the center of an image),radius
cv.imshow('circle',blank)


#DWAR A LINE
cv.line(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2),(255,255,255),thickness=5) #start point ,end point
cv.imshow('line',blank)

#HOW TO WRITE TEXT ON AN IMAGE
cv.putText(blank,'HELLO',(350,350),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),2)
# text,co-ordinates,font,font size,colour,thickness
cv.imshow('Text',blank)


cv.waitKey(0)

