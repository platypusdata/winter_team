import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

while True:
    ret, frame = capture.read()

    if ret == True :
        cv2.imshow("MyCam", frame)
        if cv2.waitKey(1) == ord('q'): break
    else :
        print('read error')

capture.release()
cv2.destroyAllWindows()