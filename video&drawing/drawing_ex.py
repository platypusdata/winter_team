import numpy as np
import cv2 as cv

img = np.zeros((512,512,3),np.uint8)
#512x512 사이즈의 검은 화면

cv.line(img,(0,0),(511,511),(0,255,0),5)

cv.rectangle(img,(100,100),(200,200),(255,0,0),2)
cv.rectangle(img,(300,100),(400,200),(255,0,0),-1)

cv.circle(img,(256,350),80,(255,255,0),-1)

cv.ellipse(img,(400,400),(50,100),0,0,360,(0,0,255),1)
#(50,100)>가로,세로

pts = np.array([[10,5], [80,50], [30,60], [10,200]], np.int32)
#왼쪽 위부터 시작, 시계방향으로 돌아감
pts = pts.reshape ((-1,1,2))
cv.polylines (img,[pts],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Hello OpenCV',(50,500), font, 2,(255,255,255),2,cv.LINE_AA)
#두께 2, 글자크기 3, (50,500)은 글자의 좌표


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
