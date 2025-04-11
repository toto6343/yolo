from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 훈련
model.train(
    data="WTDC/v6_advanced_yolo/datasets", # 훈련 데이터셋 경로
    epochs=100,
    # batch=2,
    imgsz=320,
    patience=1
)

# 데이터셋 클래스 3개 이상 학습 후 예측 확인해보기
# datasets/
#           train/
#                   class1/
#                           images...
#                   class2/
#                           images...
#                   class3/
#                           images...
#           val/
#                   class1/
#                           images...
#                   class2/
#                           images...
#                   class3/
#                           images...
#           test/
#                   class1/
#                           images...
#                   class2/
#                           images...
#                   class3/
#                           images...
#
#
# 교재
# 160 ~ 195p
# 196 ~ 198p
# 279 ~ 302p