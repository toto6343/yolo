from ultralytics import solutions
import cv2

cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/13372524_1080_1920_30fps.mp4")

speed_region = [(542, 1930), (1000, 500)]

speed_estimator = solutions.SpeedEstimator(
    model="yolo11n.pt",
    show=True,
    region=speed_region,
    line_width=3
)

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("프레임을 읽지 못했거나 영상 재생이 완료됨")
        break
    re_frame = cv2.resize(frame, (640, 840))
    cv2.namedWindow("Ultralytics Solutions", cv2.WINDOW_NORMAL)
  
    results = speed_estimator(re_frame)
    print(results)
    
cap.release()
cv2.destroyAllWindows()
