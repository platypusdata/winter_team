import cv2
import timeit
#test
# 모델 불러오기
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# 영상 파일
cam = cv2.VideoCapture(0)

# 이미지 파일
#img = cv2.imread('sample.jpg')

while True:

    start_t = timeit.default_timer()
    # 알고리즘 시작 시점

    # 캡처 이미지 불러오기
    ret, img = cam.read()
    # 영상 압축
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cascade 얼굴 탐지 알고리즘
    results = face_cascade.detectMultiScale(gray,  # 입력 이미지
                                       scaleFactor=1.1,  # 이미지 피라미드 스케일 factor
                                       minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                       minSize=(20, 20)  # 탐지 객체 최소 크기
                                       )

    for box in results:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    """ 알고리즘 연산 """
    # 알고리즘 종료 시점
    terminate_t = timeit.default_timer()
    FPS = 'fps' + str(int(1. / (terminate_t - start_t)))
    cv2.putText(img, FPS, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    # 영상 출력
    cv2.imshow('Your Face', img)

    if cv2.waitKey(1) > 0:
        break

cv2.destroyAllWindows()