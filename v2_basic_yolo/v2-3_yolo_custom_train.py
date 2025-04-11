from ultralytics import YOLO

# 1. YOLO 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 훈련
model.train(
    epochs = 10,
    data = "WTDC/v2_basic_yolo/coco8.yaml"
)
