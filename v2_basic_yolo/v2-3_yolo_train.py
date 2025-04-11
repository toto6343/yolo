from ultralytics import YOLO

# 1. YOLO 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 훈련
model.train(
    epochs = 10,
    data = "WTDC/v2_basic_yolo/coco8.yaml"
)

# 1. 데이터셋 구축
# - 라벨링
# - Train / Val : 3 / 2
# - 모델 학습 
# - 모델 확인
