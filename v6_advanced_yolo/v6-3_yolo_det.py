from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model(
    "WTDC/images/7390118689_l.jpg",
    # save=True,
    # conf=0.9 # 임계치 = Threshold
)

print(dir(results[0]))
print(dir(results[0].boxes))
print(results[0].boxes.xywh)
print(results[0].boxes.conf)
print(results[0].boxes.cls)
print(results[0].boxes.xywhn)
# 탐지된 바운딩 박스 좌표 값을 출력하기

