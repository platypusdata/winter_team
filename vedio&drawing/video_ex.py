import numpy as np
import cv2 as cv
'''
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
#웹캡에서 변환, save 불가

cap = cv.VideoCapture('sample.mp4')

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("frame을 받을 수 없습니다.")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1)==ord('q'):
        break
        
#존재하는 파일을 변환, save 불가 
'''

cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.flip(frame, -1)
    #0이 좌우(x축), 1은 상하(y축),-1은 대칭이동
    #font = cv.FONT_HERSHEY_SIMPLEX
    #cv.putText(frame, 'hello opencv', (100, 380), font, 2, (255, 255, 255), 2, cv.LINE_AA)
    #text를 영상에 삽입
    out.write(frame) #촬영되는 영상을 객체에 write
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
