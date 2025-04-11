from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")
print(model)

# 2. 모델 예측
results = model("frame_000.png")

# 3. 예측 결과 확인
print(results)
