from ultralytics import SAM

# 모델 로드
model = SAM("sam_b.pt")

# 모델 추론
model("WTDC/images/images.jpg", save=True)

