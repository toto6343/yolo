from ultralytics import YOLO
import cv2

# 모델 로드
model = YOLO("yolo11n.pt")

# 비디오 생성
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/5927708-hd_1080_1920_30fps.mp4")

# 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if success:
        # 트래킹 결과 얻기
        results = model.track(frame, persist=True, stream=True)

        for result in results:
          
            annotated_frame = result[0].plot()  # Plot the first result

            # 윈도우에 결과 출력
            cv2.namedWindow("YOLO_TRACK", cv2.WINDOW_NORMAL)
            cv2.imshow("YOLO_TRACK", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("종료")
            break
    else:
        print("프레임 확인해주세요.")
        break
        
cap.release()
cv2.destroyAllWindows()
