import cv2 as cv
img = cv.imread('PHOTOS/messi.jpg') #read an image
cv.imshow('messi',img) #used to display an image 
cv.waitKey(0)#this function makes sure that the image windows stays open usil a key is pressed
capture = cv.VideoCapture('VIDEO/sample_vid.mp4')#Take input of the video
while True:
    isTrue , frame = capture.read()
    cv.imshow('video',frame)
    if(cv.waitKey(20) & 0xFF==ord('d')):# 0XFF function is used to indicate that if 'd is pressed the video stops(terminated)
        break
capture.release()
cv.destroyAllWindows()

