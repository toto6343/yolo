from ultralytics import solutions
import cv2
import threading

# 비디오 경로 설정
video_path = "WTDC/v6_advanced_yolo/video/12617998_1920_1080_30fps.mp4"
cap = cv2.VideoCapture(video_path)

model = "yolo11n.pt"
count_points = [(100, 200), (250, 50)]

# 객체 카운팅 함수
def count_objects(frame, count_points, model, classes=[2, 3, 5]):
    counter = solutions.ObjectCounter(
        model=model,
        show=True,
        classes=classes,
        region=count_points
    )
    counter_result = counter.count(frame)  # 'frame'을 넘겨야 함
    print(f"Object Count : {counter_result}")
    return counter_result

# 객체 자르기 함수
def crop_objects(frame, model, classes=[2], crop_dir="./cropped_car"):
    cropper = solutions.ObjectCropper(
        model=model,
        show=True,
        classes=classes,
        crop_dir=crop_dir
    )
    cropper_result = cropper.crop(frame)  # 'frame'을 넘겨야 함
    print(f"Cropped and Saved to {crop_dir}")
    return cropper_result

# 객체 블러 처리 함수
def blur_objects(frame, model, classes=[0], blur_ratio=0.5):
    blurrer = solutions.ObjectBlurrer(
        model=model,
        show=True,
        blur_ratio=blur_ratio,
        classes=classes
    )
    blurrer_result = blurrer.blur(frame)  # 'frame'을 넘겨야 함
    print(f"Objects blurred with ratio {blur_ratio}")
    return blurrer_result

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break  # 비디오 끝에 도달하면 종료

    frame = cv2.resize(frame, (640, 480))

    # 멀티스레드 작업 정의
    count_thread = threading.Thread(target=count_objects, args=(frame, count_points, model))
    crop_thread = threading.Thread(target=crop_objects, args=(frame, model))
    blur_thread = threading.Thread(target=blur_objects, args=(frame, model))

    # 스레드 시작
    count_thread.start()
    crop_thread.start()
    blur_thread.start()

    # 스레드 종료 대기
    count_thread.join()
    crop_thread.join()
    blur_thread.join()

    print("Frame processing complete.")

    # 처리된 프레임 화면에 표시
    cv2.imshow('Processed Video', frame)

    # 'q' 키를 누르면 비디오 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 및 윈도우 종료
cap.release()
cv2.destroyAllWindows()
