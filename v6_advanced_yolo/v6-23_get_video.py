from ultralytics import YOLO
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/1860079-uhd_2560_1440_25fps.mp4")

points = []

# 마우스 이벤트 처리 콜백 함수 정의
def moust_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        # print(f"Clicked : {x}, {y}")
        
        if len(points) == 4:
            print(f"Points : {points}")
            # cv2.rectangle()
            points.clear()
        
# 윈도우 창 이름 설정
cv2.namedWindow("Get_Video_X_Y")

# 콜백 함수 등록
cv2.setMouseCallback("Get_Video_X_Y", moust_callback)

while True:
    success, frame = cap.read()
    if not success:
        break
    
    cv2.imshow("Get_Video_X_Y", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
