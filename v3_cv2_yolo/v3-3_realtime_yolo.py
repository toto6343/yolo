from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 카메라 해상도 설정

# 3. 모델 로드
model = YOLO("yolo11n.pt")

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("REALTIME", annotated_frame)
        
        # 'q'키를 눌러서 나가기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q를 눌러서 나갑니다.")
            break

cap.release()
cv2.destroyAllWindows()