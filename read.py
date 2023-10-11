import cv2 as cv

## Reading Image
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('Cat',img)
# cv.waitKey(0)

## Reading Video
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows() 