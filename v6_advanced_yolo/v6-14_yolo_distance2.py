from ultralytics import solutions
import cv2

# 거리 값 찾기 => dir()
# 거리에 따른 상태 정의 => if 문 사용
# print()

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("WTDC/v6_advanced_yolo/video/853889-hd_1920_1080_25fps.mp4")

# 2. 모델 로드
distance_calculator = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True
)
# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("비디오 프레임 확인")
        break
    
    frame = cv2.resize(frame, (640, 380))    
    
    results = distance_calculator(frame)
    status = "===>"
    color =  (0, 0, 0)
    
    check_distance = results.pixels_distance
    
    # 3-1. 거리 상태 정의
    if check_distance is None or check_distance == 0:
        status += "We need distance"
        color = (0, 0, 0) # 검정색
    elif check_distance >= 100:
        status += "Safe"
        color = (255, 0, 0)
    elif check_distance >= 50:
        status += "Warning"
        color = (0, 255, 255)
    else:
        status += "Danger"
        color = (0, 0, 255)
    
    print(f"Distance = {check_distance}, Status = {status}")
    
    # 상태를 프레임에 출력
    cv2.putText(
        frame, status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2
    )
    
    # 상태 표시
    cv2.imshow("Ultralytics Solutions", frame)
    cv2.waitKey(5)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. 비디오 종료 
cap.release()
cv2.destroyAllWindows()