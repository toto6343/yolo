import cv2

cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/856765-hd_1920_1080_25fps.mp4")

success, frame = cap.read()
if success:
    cv2.imwrite("parking.jpg", frame)
    
cap.release()

