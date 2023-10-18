import cv2 as cv

img = cv.imread('photos/boston.jpeg')
cv.imshow('Boston',img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur',average)

# gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur',gauss)

# median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur',median)

#bilateral 
bilateral = cv.bilateralFilter(img , 5, 15, 15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)