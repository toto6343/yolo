from ultralytics import YOLO
import cv2

# Classify, Detect, Segment
# 분류, 탐지, 분할

# 모델 로드
model = YOLO("yolo11n-seg.pt")

# 모델 예측
results = model(
    "WTDC/v6_advanced_yolo/images/dog9.jpg"
)

# 결과 저장
image = results[0].plot()
cv2.imwrite("results.jpg", image)

# segment 데이터셋 구축 방법 => 구글링 => roboflow
# 분류, 탐지, 분할 차이점

