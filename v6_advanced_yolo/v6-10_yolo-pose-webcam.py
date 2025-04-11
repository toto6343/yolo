from ultralytics import YOLO
import cv2

# 모델 로드
model = YOLO("yolo11n-pose.pt")

# 비디오 가져오기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라 연결 확인해주세요.")
    exit()
    
while True:
    success, frame = cap.read()
    if not success:
        print("프레임 확인해주세요.")
        break
       
    # YOLO 모델 예측
    results = model(frame)
       
    annotated_frame = results[0].plot()
    
    # 키 포인트 좌표 값 출력
    # print(dir(results[0]))
    print(results[0].keypoints.xy)
    
    # 영상 출력
    cv2.namedWindow("YOLO_POSE", cv2.WINDOW_NORMAL)
    cv2.imshow("YOLO_POSE", annotated_frame)
    
    # q 키를 눌러서 나가기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 리소스 해제
cap.release()
cv2.destroyAllWindows()