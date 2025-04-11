from ultralytics import YOLO
import cv2
import time

# 
models = [
    "yolov5x6u.pt",
    "yolov8n.pt",
    "yolov9t.pt",
    "yolov10x.pt",
    "yolo11n.pt"
]

image_path =  "WTDC/temp/-apt-attend_1131A_135_jpg.rf.3390587ca3eb977403318f5e3574e6d9.jpg"

for i in models:
    model = YOLO(i)
    
    start_time = time.time()
    
    results = model(image_path, save=True)
    
    end_time = time.time()
    
    inference_time = end_time - start_time
    
    image = results[0].plot()
    results_image_path = f"./result2_{i.split('.')[0]}.jpg"
    cv2.imwrite(results_image_path, image)
    
    print("-----")
    print(f"모델명 : {i}")
    print(f"시작 시간 : {start_time}")
    print(f"종료 시간 : {end_time}")
    print(f"추론시간 : {inference_time}")
    print("-----")
    