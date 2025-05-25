# annotated_frame 변수를 만들어서 영상으로 출력
import streamlit as st 
import cv2
import pandas as pd
import plotly.express as px 
from ultralytics import YOLO
import uuid
import numpy as np
import time

# 페이지 설정
st.set_page_config(
    page_title="CCTV 탐지",
    page_icon="🎥",
    layout="wide"
)

# 모델 로드 (한 번만 로드)
model = YOLO("yolov8n.pt")

# 페이지 제목
st.title("🎥 CCTV 실시간 탐지")
st.markdown("""
    <div style='text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 20px;'>
        <p>지정된 CCTV 스트림에서 객체 탐지 결과를 표시합니다.</p>
    </div>
""", unsafe_allow_html=True)

# CCTV 스트림 URL 입력
video = st.text_input("CCTV 스트림 URL을 입력하세요", "http://example.com/stream")

# 3. 프레임, 차트 출력 공간 초기화
frame_placeholder = st.empty()
chart_placeholder = st.empty()

# 4. 비디오 처리
cap = cv2.VideoCapture(video)

if not cap.isOpened():
    st.error(f"CCTV 스트림을 열 수 없습니다: {video}")
else:
    # 객체 카운트를 저장할 딕셔너리
    object_counts = {}
    
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("비디오 스트림을 더 이상 읽을 수 없습니다.")
            break
            
        # YOLO로 객체 탐지
        results = model(frame)
        
        # 탐지된 객체 카운트
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0])
                name = model.names[cls]
                if name in object_counts:
                    object_counts[name] += 1
                else:
                    object_counts[name] = 1
        
        # 결과 시각화
        annotated_frame = results[0].plot()
        
        # BGR에서 RGB로 변환
        rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        
        # 프레임 표시
        frame_placeholder.image(rgb_frame, channels="RGB")
        
        # 객체 카운트 표시
        if object_counts:
            df = pd.DataFrame(list(object_counts.items()), columns=["객체", "개수"])
            st.bar_chart(df.set_index("객체"))
        
        # 잠시 대기
        time.sleep(0.1)

    cap.release() 