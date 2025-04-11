from ultralytics import YOLO
import cv2
import timeit

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 비디오 프레임 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)

# 3. 모델 로드
model = YOLO("yolo11x.pt")

# 4. 비디오 프레임 처리
while cap.isOpened():
    suc, fr = cap.read()
    
    if suc:
        start_time=- timeit.default_timer()

        
        results = model(fr)
        
        annotated_frame = results[0].plot()
        boxes = results[0].boxes
        
        count = 0
        
        for i in boxes.cls:
            count += 1
            
        end_time = timeit.default_timer()
        
        inference_time = int(1./ (end_time - start_time))
            
        cv2.putText(
            annotated_frame, 
            f"fps : {fps}",
            (10, 30),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0), 
            cv2.LINE_AA
        )
        
        # 결과 화면 출력
        cv2.imshow("PUT_TEXT", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q를 눌러서 나갑니다.")
            break
        
cap.release()
cv2.destroyAllWindows()
