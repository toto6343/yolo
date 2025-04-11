from ultralytics import solutions
import cv2

cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/12617998_1920_1080_30fps.mp4")

isegment = solutions.InstanceSegmentation(
    model="yolo11n-seg.pt",
    show=True    
)

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    results = isegment(frame)
    print(f"results : {results}")
    print(f"isegment.track_ids : {isegment.track_ids}")
    
cap.release()
cv2.destroyAllWindows()
