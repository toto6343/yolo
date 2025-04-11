import cv2
import os
import time
from datetime import datetime
import schedule

# 1. 이미지 수집 간격
interval_time = 10

# 2. 저장 디렉토리 설정
SAVE_DIR = "capture_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# 3. 데이터 수집 함수
def capture_image():
    # 3-1. 카메라 불러오기
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv007.stream/playlist.m3u8")
    # 3-2. 카메라 확인
    if not cap.isOpened():
        raise RuntimeError("카메라 확인해주세요")
    
    print("카메라 연결 완료")
    
    # 3-3. 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        print("OPEN")
        timestamp = datetime.now().strftime("%Y%m&d_%H%M")
        file_path = os.path.join(SAVE_DIR, f"{timestamp}.jpg")
        
        # 3-4. 수집 이미지 저장
        cv2.imwrite(file_path, frame)
        print(f"사진이 저장 됐습니다.{file_path}")
    else:
        print("프레임을 못 읽었습니다.")
        
    # 3-5. 카메라 해제
    cap.release()
    cv2.destroyAllWindows()
    print(f"{interval_time}초 간격으로 이미지를 수집합니다.")
 
capture_image()
   
# Schedule 실행 설정
schedule.every(interval_time).seconds.do(capture_image)

while True:
    schedule.run_pending()
    time.sleep(1)
    
