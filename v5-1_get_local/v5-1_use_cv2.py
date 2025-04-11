import cv2
import os
from datetime import datetime

# 1. 저장할 디렉토리 설정
SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# 2. 카메라 불러오기
cap = cv2.VideoCapture('http://210.99.70.120:1935/live/cctv006.stream/playlist.m3u8')

# 3. 카메라 확인
if not cap.isOpened():
    raise RuntimeError("카메라 연결 안됨")

print("카메라 연결 됐습니다.")

# 4. 카메라 프레임 읽기
success, frame = cap.read()
if success:
    print("OPEN")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    file_path = os.path.join(SAVE_DIR, f"get_{timestamp}.jpg")
    
    # 5. 이미지 저장
    cv2.imwrite(file_path, frame)
    print(f"사진이 저장 됐습니다. {file_path}")
else:
    print("프레임 못 읽습니다.")
    
# 6. 카메라 해제
cap.release()
cv2.destroyAllWindows()
    
