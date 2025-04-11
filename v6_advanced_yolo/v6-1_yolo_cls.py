from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("runs/classify/train5/weights/best.pt")

# 2. 모델 예측
results = model(
    "WTDC/images/201108288_1280.jpg",
    save=True
)

# 3. 이미지 저장
image = results[0].plot()
cv2.imwrite("result_image_cls.jpg", image)

