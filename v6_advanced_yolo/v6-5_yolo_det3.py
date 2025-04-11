from ultralytics import YOLO
import cv2
import timeit

# 1. 비디오 경로 설정 (웹캠을 사용할 경우 0, 또는 비디오 파일 경로 입력)
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv006.stream/playlist.m3u8")

# 2. 비디오 프레임 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 4. 비디오 프레임 처리
while cap.isOpened():
    suc, fr = cap.read()
    
    if suc:
        start_time = timeit.default_timer()
      
        # 모델 예측 수행
        results = model(fr)
        
        # 예측 결과로 주석 달기
        annotated_frame = results[0].plot()
        
        boxes = results[0].boxes
               
        end_time = timeit.default_timer()
        
        # 추론 시간 계산
        inference_time = int(1./ (end_time - start_time))
        
        
        # 상태 정의
        number = len(results[0])
        # print(f"탐지된 개수 {number}")
        if number <= 2:
            status = "Normal"
        elif 3 <= number <= 6:
            status = "Warning"
        else:
            status = "Danger"
                   
        # 화면에 출력할 상태 텍스트 정의
        status_text = [
            f"FPS: {inference_time}",
            # f"Inference Time: {inference_time:.2f} sec",
            f"Objects Detected: {number}, Status: {status}"
        ]
        
        # 텍스트 위치 설정
        y_position = 30
        
        # 상태 텍스트를 화면에 출력
        for text in status_text:
            cv2.putText(
                annotated_frame,  # 출력할 이미지
                text,              # 출력할 텍스트
                (10, y_position),  # 텍스트 위치
                cv2.FONT_HERSHEY_COMPLEX,  # 폰트
                1,                  # 글자 크기
                (0, 255, 0),       # 글자 색 (녹색)
                2,                  # 두께
                cv2.LINE_AA         # 선 종류
            )
            y_position += 30  # 각 텍스트의 y 위치를 30px씩 아래로 내려감
        
        # 결과 화면 출력
        cv2.imshow("PUT_TEXT", annotated_frame)
        
        
        
        # 'q' 키를 눌러서 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q를 눌러서 나갑니다.")
            break

# 비디오 캡처 해제 및 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
