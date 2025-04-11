from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")  # YOLOv11 모델 로드

# 2. 모델 예측
results = model(
    "WTDC/v6_advanced_yolo/pexels-little-forest-2150377525-31249687.jpg",  # 이미지 파일 경로
    save=True,
    # classes=60,
    classes=[41, 60]        
)


