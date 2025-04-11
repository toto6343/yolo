from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/853889-hd_1920_1080_25fps.mp4")

# blurr 객체 생성
blurrer = solutions.ObjectBlurrer(
    model="yolo11n.pt",
    show=True,
    blur_ratio=0.5
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    re_frame = cv2.resize(frame, (640, 480))
    results = blurrer(frame)
    
cap.release()
cv2.destroyAllWindows()
