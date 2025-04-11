from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import base64
import cv2
from ultralytics import YOLO
from datetime import datetime

# 모델 로드
model = YOLO("yolo11n.pt")

# 데이터 저장할 리스트
x_data = []
y_data = []

# Dash 애플리케이션 초기화
app = Dash(__name__)

# 대시보드 레이아웃 정의
app.layout = html.Div(
    style={"backgroundColor": "#f0f4f8", "padding": "40px"},  # 전체 배경 색상과 패딩
    children=[
        html.H1(
            "Dash YOLO 탐지 대시보드",
            style={
                "textAlign": "center",
                "color": "#333",
                "fontSize": "40px",
                "fontWeight": "bold",
                "marginBottom": "30px",
                "borderBottom": "3px solid #ff7f50",  # 제목 아래에 강조선 추가
                "paddingBottom": "15px"
            }
        ),
        html.Div(
            children=[
                html.Img(
                    id="live-detection-image",
                    style={
                        "width": "100%",
                        "maxWidth": "1200px",  # 최대 크기 제한
                        "margin": "auto",
                        "display": "block",
                        "borderRadius": "15px",  # 부드러운 모서리 처리
                        "boxShadow": "0px 10px 30px rgba(0, 0, 0, 0.1)",  # 그림자 효과
                        "border": "5px solid #ff7f50"  # 이미지 테두리 색상 추가
                    }
                )
            ],
            style={
                "textAlign": "center",
                "marginBottom": "40px"
            }
        ),
        dcc.Graph(
            id="Dash-Yolo-Graph",
            style={
                "height": "500px",
                "borderRadius": "15px",
                "backgroundColor": "#fff",  # 그래프 배경색
                "boxShadow": "0px 10px 30px rgba(0, 0, 0, 0.1)",  # 그래프 그림자 효과
                "padding": "20px"
            }
        ),
        dcc.Interval(
            id="update-interval",
            interval=1000,  # 1초마다 업데이트
            n_intervals=0
        )
    ]
)

# 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv036.stream/playlist.m3u8")

# 콜백 함수 정의
@app.callback(
    [
        Output("live-detection-image", "src"),
        Output("Dash-Yolo-Graph", "figure")
    ],
    [
        Input("update-interval", "n_intervals")
    ]
)
def update_frame(n_intervals):
    global cap

    # 프레임 읽기
    success, frame = cap.read()
    if not success:
        print("비디오 스트림 읽기 실패")
        return None, go.Figure()  # 연결 실패 시 빈 그래프 반환

    # 객체 탐지 수행
    results = model(frame)

    # 객체 탐지 수 계산
    num = len(results[0].boxes)

    # 탐지 결과를 이미지에 표시
    annotated_frame = results[0].plot()

    # 이미지 => 인코딩 => Base64
    _, buffer = cv2.imencode('.jpg', annotated_frame)
    frame_base64 = base64.b64encode(buffer).decode()

    # 현재 시간 가져오기
    current_time = datetime.now().strftime("%Y%m%d_%H:%M")

    # 시간과 탐지된 객체 수를 추가 저장
    x_data.append(current_time)
    y_data.append(num)

    # 실시간 그래프 데이터 생성
    figure = {
        'data': [
            go.Scatter(
                x=x_data,  # 시간 데이터
                y=y_data,  # 탐지된 객체 수
                mode='lines+markers',  # 선과 마커를 모두 표시
                marker={'color': '#ff7f50', 'size': 8}  # 마커 색상과 크기
            )
        ],
        'layout': go.Layout(
            title="실시간 탐지 수 변화",  # 그래프 제목
            xaxis={
                "title": "시간",  # x축 제목
                "tickangle": 45,  # x축 tick 라벨 각도
                "title_font": {"size": 14},  # x축 제목 글꼴 크기 (수정된 부분)
                "tickfont": {"size": 12}  # x축 tick 라벨 글꼴 크기
            },
            yaxis={
                "title": "탐지 수",  # y축 제목
                'dtick': 1,  # y축 tick 간격
                "tickfont": {"size": 12}  # y축 tick 라벨 글꼴 크기
            },
            template="plotly_dark",  # 어두운 테마
            plot_bgcolor="#2e2e2e",  # 그래프 배경 색상
            paper_bgcolor="#333",  # 차트 외부 배경 색상
            font={"color": "white"},  # 그래프의 글자 색상
            margin={"l": 40, "r": 40, "t": 40, "b": 40}  # 그래프 여백 설정
        )
    }

    return f"data:image/jpeg;base64,{frame_base64}", figure

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)
