from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/853889-hd_1920_1080_25fps.mp4")

# 거리 계산 객체 생성
distance_calculator = solutions.DistanceCalculation(
    model='yolo11n.pt',
    show=True
)

# 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("비디오 프레임 확인")
        break
    
    frame_resized = cv2.resize(frame, (640, 360))
    results = distance_calculator(frame_resized)
    
    
cap.release()
cv2.destroyAllWindows()
