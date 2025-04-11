from ultralytics import YOLO
import cv2
import threading
import time, timeit
import os  # os 라이브러리를 사용하여 파일명을 추출

# 비디오 경로 설정
video_file1 = "WTDC/v6_advanced_yolo/video/5927708-hd_1080_1920_30fps.mp4"
video_file2 = "WTDC/v6_advanced_yolo/video/13372524_1080_1920_30fps.mp4"
video_file3 = "WTDC/v6_advanced_yolo/video/13366588_2160_3840_30fps.mp4"

# 모델 로드
model1 = YOLO("yolo11n.pt")
model2 = YOLO("yolov10x.pt")
model3 = YOLO("yolov9t.pt")

# 모델 파일명에서 모델 이름만 추출하는 함수
def get_model_name(model):
    # 모델 파일의 경로에서 확장자를 제외한 모델 이름만 추출
    model_file = model.weights if hasattr(model, 'weights') else ''
    model_name = os.path.splitext(os.path.basename(model_file))[0]  # .pt 확장자 제거
    return model_name

# 비디오 파일 처리 및 객체 추적 실행 함수
def run_tracker(filename, model, file_index):
    cap = cv2.VideoCapture(filename)
    
    # FPS 계산용 변수 초기화
    frame_count = 0
    prev_time = time.time()

    # 비디오가 열려 있는 동안 프레임을 반복해서 처리
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        start_time = timeit.default_timer()
        
        end_time = timeit.default_timer()
        
        fps = int(1./(end_time - start_time))
        
        print(fps)
        print(model)
        print(dir(model))
        
        # 객체 탐지
        results = model.track(frame, persist=True)
        res_plotted = results[0].plot()
        frame = cv2.resize(frame, (640, 380))
               
        # 창 크기 조절
        res_resized = cv2.resize(res_plotted, (640, 480))
        
        # 화면에 FPS, 모델명 표시
        cv2.putText(res_resized , f"FPS : {fps}, Model : {model.ckpt_path}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # 화면 표시       
        cv2.imshow(f"Tracking_Multi_YOLO{file_index}", res_resized)
        
        # q 키 눌러서 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

# 스레드 생성
thread1 = threading.Thread(target=run_tracker, args=(video_file1, model1, 1), daemon=True)
thread2 = threading.Thread(target=run_tracker, args=(video_file2, model2, 2), daemon=True)
thread3 = threading.Thread(target=run_tracker, args=(video_file3, model3, 3), daemon=True)

# 스레드 실행
thread1.start()
thread2.start()
thread3.start()

# 스레드 종료 대기
thread1.join()
thread2.join()
thread3.join()
