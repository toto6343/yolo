from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model(
    "WTDC/v6_advanced_yolo/images/dog1.jpg",
    max_det=10,
    conf=0.5,
    save_txt=True,
    save_conf=True,
    save_crop=True,
    save=True,
    imgsz=640
    # probs=True,
    # masks=True,
    #txt_color=
)

