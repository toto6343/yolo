from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8")

count_points = [(100, 200), (250, 50)] # line
# count_points = [(), (), (), ()] # rectangle 
# count_points = [(), (), (), (), (), ()] # polygon

counter = solutions.ObjectCounter(
    model="yolo11n.pt",
    show=True,
    region=count_points
    # classes=[]
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    results = counter(frame)
    
cap.release()
cv2.destroyAllWindows()
