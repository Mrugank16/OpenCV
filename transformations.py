import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat',img)

## translation
# def translate(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimentions = (img.shape[1] , img.shape[0])
#     return cv.warpAffine(img, transMat, dimentions)

# # -x -> left
# # -y -> up
# # x -> right
# # y -> down

# translated = translate(img, 100, 100)
# cv.imshow('Translated',translated)

## rotation
# def rotate(img, angle, rotPoint=None):
#     (height,width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimentions = (width,height)

#     return cv.warpAffine(img, rotMat, dimentions)

# rotated = rotate(img, 45)
# cv.imshow('Rotated',rotated)

## resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

## flipping
# flip0 = cv.flip(img, 0)
# cv.imshow('Vertically',flip0)
# flip1 = cv.flip(img,1)
# cv.imshow('Horizontaly',flip1)
# flip = cv.flip(img,-1)
# cv.imshow('Both Ways',flip)

## cropping
cropped = img[20:30 , 30:40]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
