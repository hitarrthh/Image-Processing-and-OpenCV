import cv2 as cv
img = cv.imread('PHOTOS/messi.jpg')
cv.imshow('messi',img)
def rescale(frame,scale_val=0.2):
    # USED IN IMAGES, VIDEOS, LIVE VIDEOS
    width = int (frame.shape[1]  * scale_val) #shape[1] = width of frame
    height = int(frame.shape[0] * scale_val)#shape[0] = height of frame
    dim = (width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
img_rescaled = rescale(img)
cv.imshow('image_rescaled',img_rescaled)


capture = cv.VideoCapture('VIDEO/sample_vid.mp4')
def change_res(width,height):
    #USEFUL FOR LIVE VIDEOS ONLY
    capture.set(3,width)
    capture.set(4,height)
while True:
    isTrue , frame = capture.read()
    frame_resized = rescale(frame)
    cv.imshow('video',frame)
    cv.imshow('v_rescaledideo',frame_resized)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()

