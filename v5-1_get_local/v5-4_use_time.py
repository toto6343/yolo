import cv2
import os
from datetime import datetime
import time

# 1. 저장 디렉토리 설정
SAVE_DIR = "captured_image"
os.makedirs(SAVE_DIR, exist_ok=True)

# 사진 간격 설정
capture_interval = 10
last_capture_time = 0

# 2. 카메라 불러오기
def capture_image():
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv005.stream/playlist.m3u8")
    
    if not cap.isOpened():
        raise RuntimeError("카메라 연결 안됨")
    
    print("카메라 연결 됐습니다.")
    
    # 3. 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(SAVE_DIR, f"time_{timestamp}.jpg")
        
        # 4. 이미지 저장
        cv2.imwrite(file_path, frame)
        print(f"사진이 저장됐습니다.{file_path}")
    else:
        print("카메라 연결 안됩니다.")
        
    # 4. 카메라 연결 해제
    cap.release()
    cv2.destroyAllWindows()

while True:
    current_time = time.time()
    # 설정된 간격으로 이미지 수집
    if current_time - last_capture_time >= capture_interval:
        capture_image()
        last_capture_time = current_time
        
    time.sleep(1)
    