import numpy as np
import cv2 as cv
img = cv.imread('ima2.jpg')

#픽셀값 접근, 수정
px = img[100,100]
print( px )

blue = img[100,100, 0]
print( blue )

img[100,100] = [255,255,255]
print( img[100,100] )

print(img.item(10,10,2))

img.itemset((10,10,2),100)
print(img.item(10,10,2))

#이미지 속성에 접근

print( img.shape )

print( img.size )

print( img.dtype )

#RoI

ball = img[301:407, 697:746]
img[100:206, 273:322] = ball

#cv.imshow("Display window", img)
#k = cv.waitKey(0)

#이미지 분리 병합
b, g, r=cv.split(img)
img = cv.merge((b,g,r))

b = img[:,:,0]

#cv.imshow("Display window", r)
#k = cv.waitKey(0)

img[:,:,2] = 0
cv.imshow("Display window", img)
k = cv.waitKey(0)
