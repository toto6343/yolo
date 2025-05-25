import streamlit as st
# import pandas as pd # 메인 페이지에서 사용하지 않음
# import mysql.connector # 메인 페이지에서 사용하지 않음
# import altair as alt # 메인 페이지에서 사용하지 않음
# import folium # 메인 페이지에서 사용하지 않음
# from streamlit_folium import folium_static # 메인 페이지에서 사용하지 않음
# from folium.plugins import MarkerCluster # 메인 페이지에서 사용하지 않음

# 다중 페이지 앱에서는 다른 페이지 임포트가 필요하지 않음
# import process_mapdata_to_db
# import map_dashboard

# 데이터베이스 연결 함수는 특정 페이지에서만 필요함
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="123456",
#         database="roadkill_db",
#         auth_plugin="caching_sha2_password"
#     )

# def get_roadkill_data():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT latitude, longitude, year, address1, address2, address3, description FROM roadkill")
#     data = cursor.fetchall()
#     df = pd.DataFrame(data, columns=["latitude", "longitude", "year", "address1", "address2", "address3", "description"])
#     cursor.close()
#     conn.close()
#     return df

# def get_roadkill_stat_data():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT year, month, region, road_type, animal, count, stat_type FROM roadkill_stats")
#     data = cursor.fetchall()
#     df = pd.DataFrame(data, columns=["year", "month", "region", "road_type", "animal", "count", "stat_type"])
#     cursor.close()
#     conn.close()
#     return df

# 페이지 설정
st.set_page_config(
    page_title="로드킬 대시보드",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 스타일 설정
st.markdown("""
    <style>
    [data-testid="stSidebar"][aria-expanded="true"]{
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 페이지 내용
st.title("🚗 로드킬 발생 현황 통합 대시보드")

st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
        <h3>환영합니다!</h3>
        <p>사이드바 메뉴에서 원하는 페이지를 선택하여 이동하세요.</p>
    </div>
""", unsafe_allow_html=True)

# 페이지 설명
st.markdown("""
    ### 📊 대시보드 구성
    - **통계 데이터**: 로드킬 발생 현황에 대한 다양한 통계와 지도 시각화
    - **지도 데이터**: 로드킬 발생 위치를 지도에서 확인
    - **웹캠 탐지**: 실시간 웹캠을 통한 객체 탐지
    - **CCTV 탐지**: CCTV 스트림을 통한 실시간 객체 탐지
""")

# 다중 페이지 앱의 메인 파일에서는 __main__ 블록이 필요하지 않습니다
# if __name__ == "__main__":
#     create_dashboard()
