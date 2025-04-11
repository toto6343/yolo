import cv2

# 이미지 파일 경로 설정
img_path = "WTDC/v6_advanced_yolo/images/dog6.jpg"

# 이미지 읽기
image = cv2.imread(img_path)
print(image.shape)

resize_image = cv2.resize(image, (640, 480))

# 마우스 이벤트 함수 정의
def mouse_callback(event, x, y, flags, param):
    # 마우스 왼쪽 버튼 클릭 이벤트 처리
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked : {x}, {y}")
    

# 윈도우 생성
cv2.namedWindow("Image_Get_X_Y")

# 콜백 함수 등록
cv2.setMouseCallback("Image_Get_X_Y", mouse_callback)

# 화면 표시 및 종료
while True:
    cv2.imshow("Image_Get_X_Y", resize_image)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 창 닫기
cv2.destroyAllWindows()

# Clicked : 237, 32
# Clicked : 198, 28
# Clicked : 119, 74
# Clicked : 164, 131