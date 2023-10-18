import cv2 as cv
import numpy as np

img = cv.imread('photos/boston.jpeg')
cv.imshow('Boston',img)

# print(img.shape)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank',blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 70, 255, -1)
# cv.imshow('Mask',mask)

# masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked',masked)

rectangle = cv.rectangle(blank.copy(), (0,0), (161,157), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape',weird_shape)

masked = cv.bitwise_and(img, img, mask = weird_shape)
cv.imshow('Masked Image',masked)

cv.waitKey(0)