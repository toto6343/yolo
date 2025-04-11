from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/853889-hd_1920_1080_25fps.mp4")

# crop 객체 생성
cropper = solutions.ObjectCropper(
    model="yolo11n.pt",
    show=True,
    classes=[0, 2]
    # crop_dir="./cropped"
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    # re_frame = cv2.resize(frame, (640, 480))
    results = cropper(frame)
    print(results)
    
cap.release()
cv2.destroyAllWindows()
