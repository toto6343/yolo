from ultralytics import YOLO
import cv2
from ultralytics.solutions import RegionCounter

# 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/1860079-uhd_2560_1440_25fps.mp4")

# 특정 좌표 설정
region_points = {
    "region-01": [(10, 500), (10, 100), (100, 500), (100, 100)],
    "region-02": [(50, 50), (50, 200), (200, 200), (200, 50)],
    "region-03": [(300, 100), (300, 250), (450, 250), (450, 100)],
    "region-04": [(100, 300), (100, 350), (500, 350), (500, 300)]
}

# YOLO 모델 불러오기
model = YOLO("yolo11n.pt")  # 모델 파일 경로

# RegionCounter 객체 생성
region = RegionCounter(
    model="yolo11n.pt",  # YOLO 모델을 넣어줍니다.
    region=region_points,
    show=True
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # 비디오 크기 조정
    frame = cv2.resize(frame, (640, 360))
    cv2.namedWindow("Ultralytics Solution", cv2.WINDOW_NORMAL)
    
    img0 = region(frame)
    
    # 특정 구역 계산
    region1 = region.region_counts.get(("region-01"), 0)
    region2 = region.region_counts.get(("region-02"), 0)
    region3 = region.region_counts.get(("region-03"), 0) 
    region4 = region.region_counts.get(("region-04"), 0)   
    print(f"region1 : {region1}, region2 : {region2}, region3 : {region3}, region4 : {region4}") # 해당 구역의 객체 수 출력
    
    re_frame = cv2.resize(frame, (640, 480))
    cv2.namedWindow("Ultralytics Solutions", cv2.WINDOW_NORMAL)
    
    cv2.putText (
        re_frame,
        f"region1 : {region1}, region2 : {region2}, region3 : {region3}, region4 : {region4}",
        cv2.FONT_HERSHEY_SIMPLEX,
        cv2.LINE_AA
    )
    
    im0 = region(re_frame)


    # 영상 출력
    cv2.imshow("Ultralytics Solutions", frame)
    cv2.waitKey()

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 해체
cap.release()
cv2.destroyAllWindows()
