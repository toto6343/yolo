import streamlit as st
import pandas as pd
import mysql.connector
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# 페이지 설정
st.set_page_config(
    page_title="로드킬 지도",
    page_icon="🗺️",
    layout="wide"
)

# MySQL 연결 함수
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="roadkill_db",
        auth_plugin="caching_sha2_password"
    )

# DB에서 roadkill_map 데이터를 가져오는 함수
def get_roadkill_map_data():
    conn = get_db_connection()
    query = "SELECT latitude, longitude, location, animal_name FROM roadkill_map WHERE latitude IS NOT NULL AND longitude IS NOT NULL"
    df_map = pd.read_sql(query, conn)
    conn.close()
    df_map['latitude'] = pd.to_numeric(df_map['latitude'], errors='coerce')
    df_map['longitude'] = pd.to_numeric(df_map['longitude'], errors='coerce')
    df_map['animal_name'] = df_map['animal_name'].fillna('동물').replace({'': '동물'})
    return df_map.dropna(subset=['latitude', 'longitude'])

# 페이지 제목
st.title("🗺️ 로드킬 지도")
st.markdown("""
    <div style='text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 20px;'>
        <p>roadkill_map 테이블의 데이터를 지도에 표시하고 검색 기능을 제공합니다.</p>
    </div>
""", unsafe_allow_html=True)

df_map = get_roadkill_map_data()

if not df_map.empty:
    # 검색창 추가
    search_term = st.text_input("동물 이름으로 검색", "").lower()

    # 검색어 필터링
    if search_term:
        filtered_df_map = df_map[df_map['animal_name'].str.contains(search_term, case=False, na=False)]
    else:
        filtered_df_map = df_map

    if not filtered_df_map.empty:
        # 중심점 계산
        center_lat = filtered_df_map['latitude'].mean()
        center_lon = filtered_df_map['longitude'].mean()

        # Leaflet 지도 생성
        m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

        # 마커 클러스터 추가
        marker_cluster = MarkerCluster().add_to(m)

        # 데이터 포인트 추가
        for idx, row in filtered_df_map.iterrows():
            animal_display = row['animal_name'] if pd.notna(row['animal_name']) and row['animal_name'] != '' else '동물'
            popup_text = f"""
            <b>위치:</b> {row['location'] if pd.notna(row['location']) else '정보 없음'}<br>
            <b>동물:</b> {animal_display}
            """
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(popup_text, max_width=300),
                tooltip=f"{row['location'] if pd.notna(row['location']) else '정보 없음'} - {animal_display}"
            ).add_to(marker_cluster)

        # 지도 표시
        folium_static(m, width=800, height=600)
    else:
        st.warning("검색 조건과 일치하는 로드킬 데이터가 없습니다.")
else:
    st.warning("로드킬 지도 데이터가 없습니다. 'CSV 처리' 페이지에서 데이터를 먼저 로드해주세요.") 