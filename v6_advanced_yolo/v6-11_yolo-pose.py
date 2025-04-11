from ultralytics import YOLO
import cv2

# 모델 로드
model = YOLO("yolo11n-pose.pt")

# 모델 훈련
results = model.train(
    data="hand-keypoints.yaml", 
    epochs=50, 
    imgsz=300,
    batch=2
)

# epochs, imasz, batch 변경해보기
# Train할 때, 데이터 imgsz => Predict imgsz = 320


