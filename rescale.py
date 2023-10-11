import cv2 as cv

def rescaleFrame(frame , scale=0.75):
    # works for images , video and Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # only works for live video
    capture.set(3,width)
    capture.set(4,height)

## Reading and resizing Video
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue , frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.2)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows() 


## Reading and resizing photo
img = cv.imread('photos/cat.jpeg')
img_resized = rescaleFrame(img)
cv.imshow('Cat',img)
cv.imshow('Cat Resized',img_resized)
cv.waitKey(0)