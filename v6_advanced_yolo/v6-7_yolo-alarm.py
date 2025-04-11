from ultralytics import solutions
import cv2

cap = cv2.VideoCapture('http://210.99.70.120:1935/live/cctv006.stream/playlist.m3u8')

from_email = "toto6343@gmail.com"
password = "xuds sbha hltq hjbl"
to_email = "toto6343@gmail.com"

security = solutions.SecurityAlarm(
    model='yolo11n.pt',
    record=1,
    show=True
)

security.authenticate(from_email, password, to_email)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # result_data = security.monitor(frame)
        result_data = security(frame)
        # cv2.imshow("YOLO", result_data)
    else:
        print("프레임 처리 실패")
        break

cap.release()
cv2.destroyAllWindows()