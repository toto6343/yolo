from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model(
    "WTDC/images/201108288_1280.jpg"
)

# 3. 상태 정의
number = len(results[0])
# print(f"탐지된 개수 {number}")
if number <= 2:
    status = "Normal"
elif 3 <= number <= 6:
    status = "Warning"
else:
    status = "Danger"
    
print(f"탐지된 개수 : {number}, 상태는 {status}입니다.")
