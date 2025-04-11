from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture("WTDC/v2_basic_yolo/video_datasets/final_video.mp4")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps = cap.get(cv2.CAP_PROP_FPS)

model = YOLO("yolo11n.pt")

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        
        print(f"FPS : {fps}")
        cv2.namedWindow("VIDEO", cv2.WINDOW_NORMAL)
        cv2.imshow("VIDEO", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
cap.release()
cv2.destroyAllWindows()
