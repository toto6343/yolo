from flask import Flask, Response
import cv2
from ultralytics import YOLO

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 모델로드
model = YOLO("yolo11n.pt")

# 비디오 시작
def generate_frame():
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv045.stream/playlist.m3u8")
    
    while True:
        success, frame = cap.read()
        if not success:
            print("FRAME CHECK")
            break
        
        # 객체 탐지
        results = model(frame)
        
        # 탐지 표시
        annotated_frame = results[0].plot()
        
        # 프레임을 인코딩
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        
        # 인코딩을 바이트
        frame_bytes = buffer.tobytes()
        
        # 데이터 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
               )
        
    cap.release()
        
# Flask 라우트 정의
@app.route('/')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 애플리케이션 실행
if __name__ == "__main__":
    # Flask 서버를 실행
    app.run(host='0.0.0.0', port=5000, debug=True)
        