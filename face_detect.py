import cv2 as cv

img = cv.imread('photos/many.jpeg')
cv.imshow('Group of many people',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img , (x,y), (x+w,y+w), (0,255,0), thickness=2)

cv.imshow('Detected faces',img)

cv.waitKey(0)