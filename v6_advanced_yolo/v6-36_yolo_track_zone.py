from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/854745-hd_1280_720_50fps.mp4")

# 비디오 정보 가져오기
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter(
    "trackzone.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (w, h)
)

# 구역 설정
region_points = [(500, 0), (500, 200), (600, 400)]

# TrackZone 객체 생성
trackzone = solutions.TrackZone(
    model="yolo11n.pt",
    region=region_points,
    show=False,
    classes=[2, 3, 5]
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    Results = trackzone(frame)
    video_writer.write(Results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()

