from sahi.utils.file import download_from_url
from sahi.utils.ultralytics import download_yolo11n_model
from sahi.predict import get_prediction
from sahi import AutoDetectionModel

# 모델 다운로드
model_path = "yolo11n.pt"
download_yolo11n_model(model_path)

# 테스트 이미지 다운로드
# download_from_url(
#    "https://github.com/obss/sahi/blob/main/demo/demo_data/small-vehicles1.jpeg",
#    "test.jpeg"
#)

# 모델 로드
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path
)

# 모델 예측
results = get_prediction(
    "demo_data/small-vehicles1.jpeg",
    detection_model
)

# 모델 예측 결과 저장
results.export_visuals(export_dir="sahi/default")
print("=============")
print("SAHI_SUCCESS")