import streamlit as st 
import cv2
import pandas as pd
import plotly.express as px  
from ultralytics import YOLO

# 모델 로드
model = YOLO("yolo11n.pt")

# Streamlit 레이아웃 설정
st.set_page_config(layout="wide")
st.title("YOLO 실시간 탐지 대시보드")

# 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 객체 탐지 결과 저장 리스트
detections = []

# 프레임, 차트 출력 공간
frame_placeholder = st.empty()
chart_placeholder = st.empty()

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("FRAME CHECK")
        st.error("ST_FRAME CHECK", icon="O")
        break
    
    # 객체 탐지
    results = model(frame)
    
    # 탐지된 객체를 저장 리스트
    detected_object = []
    for result in results:
        for box in result.boxes:
            cls = model.names[int(box.cls[0])]
            detected_object.append(cls)

            # 바운딩 박스 그리기
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            label = f"{cls} {conf:.2f}"
            
            # 박스, 텍스트 추가
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, label, (x1, y1 -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # 탐지된 객체 리스트를 전체 탐지 결과에 추가
    detections.append(detected_object)
    
    # 프레임을 RGB로 변환
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Streamlit에서 이미지 표시
    frame_placeholder.image(frame, channels="RGB", use_container_width=True)
    
    # 1개 프레임에서 탐지된 객체를 통합
    all_objects = [obj for sublist in detections[-1:] for obj in sublist]
    
    # 풀어서 사용하면
    # all_objects = []
    # for sublist in detections[-1:]:
    #    for obj in sublist:
    #        all_objects.append(obj)
    
    # 각 객체별로 수량을 계산
    object_count = pd.DataFrame({"객체": all_objects}).value_counts().reset_index()
    object_count.columns = ["객체", "수량"]
    
    # 그래프 그리기
    fig = px.bar(object_count, x='객체', y='수량', title='탐지된 객체 통계', text_auto=True)
    
    # 중복 피하기
    chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"chart_{len(detections)}")
    
        

