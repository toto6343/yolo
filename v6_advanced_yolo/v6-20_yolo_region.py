from ultralytics import solutions
import cv2

# 이미지 파일 열기
im0 = cv2.imread("WTDC/images/201108288_1280.jpg")
im0 = cv2.resize(im0, (640, 480))

# 좌표 설정
region_points = {
    # "region-01" : [(10, 30), (100, 30), (10, 100), (100, 100)]
    "region-01" : [(10, 30), (119, 74), (100, 100), (164, 131)], 
    "region-02" : [(10, 30), (200, 80), (40, 90), (124, 10)],
    "region-03" : [(10, 30), (100, 30), (10, 100), (100, 100)],
    "region-04" : [(20, 50), (100, 200), (200, 100), (90, 30)],
    "region-05" : [(200, 150), (300, 100), (500, 200), (250, 300)],
    "region-06" : [(500, 300), (450, 600), (200, 400), (640, 480)],
}

# Clicked : 237, 32
# Clicked : 198, 28
# Clicked : 119, 74
# Clicked : 164, 131

# RegionCounter 객체 생성
region = solutions.RegionCounter(
    model="yolo11n.pt",
    show=True,
    region=region_points
)

# Region 계산
results = region(im0)
print(results)
cv2.waitKey(0)
cv2.imwrite("results.jpg", results)
