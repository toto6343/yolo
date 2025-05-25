import streamlit as st
import pandas as pd
import mysql.connector
import altair as alt
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# 페이지 설정
st.set_page_config(
    page_title="로드킬 통계",
    page_icon="📊",
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

# DB에서 로드킬 데이터를 가져오는 함수
def get_roadkill_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT latitude, longitude, year, address1, address2, address3, description FROM roadkill")
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["latitude", "longitude", "year", "address1", "address2", "address3", "description"])

    cursor.close()
    conn.close()
    return df

def get_roadkill_stat_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT year, month, region, road_type, animal, count, stat_type FROM roadkill_stats")
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["year", "month", "region", "road_type", "animal", "count", "stat_type"])

    cursor.close()
    conn.close()
    return df

# 페이지 제목
st.title("로드킬 통계")
st.markdown("""
    <div style='text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 20px;'>
        <p>로드킬 발생에 대한 다양한 통계 데이터를 보여줍니다.</p>
    </div>
""", unsafe_allow_html=True)

# 통계 데이터 관련 코드
df = get_roadkill_data()
df_stat = get_roadkill_stat_data()

# 연도 선택 (지도와 통계 모두에 사용)
selected_year = st.selectbox(
    "연도 선택",
    options=sorted(df["year"].unique(), reverse=True),
    index=0
)

# 선택된 연도의 데이터만 필터링
df_filtered = df[df["year"] == selected_year]

# 지도 섹션
st.subheader(f"{selected_year}년 로드킬 발생 위치")
if not df_filtered.empty:
    # 중심점 계산
    center_lat = df_filtered['latitude'].mean()
    center_lon = df_filtered['longitude'].mean()

    # Leaflet 지도 생성
    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

    # 마커 클러스터 추가
    marker_cluster = MarkerCluster().add_to(m)

    # 데이터 포인트 추가
    for idx, row in df_filtered.iterrows():
        popup_text = f"""
        <b>위치:</b> {row['address3'] if pd.notna(row['address3']) else '정보 없음'}<br>
        <b>상세 위치:</b> {row['description'] if pd.notna(row['description']) else '정보 없음'}
        """
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=f"{row['address3'] if pd.notna(row['address3']) else '정보 없음'}"
        ).add_to(marker_cluster)

    # 지도 표시
    folium_static(m, width=800, height=600)
else:
    st.warning(f"{selected_year}년 데이터가 없습니다.")

# 통계 섹션
st.subheader("지역별 발생 현황")
address3_counts = df_filtered['address3'].value_counts()
st.bar_chart(address3_counts)

st.subheader("연도별 발생 현황")
year_stats_df = df_stat[df_stat["stat_type"] == "연도별"]
if not year_stats_df.empty:
    year_stats_df = year_stats_df.pivot_table(index='year', values='count', aggfunc='sum')
    st.bar_chart(year_stats_df)
else:
    st.write("연도별 통계 데이터가 없습니다.")

st.subheader("월별 로드킬 추이 꺾은선 그래프")
month_df = df_stat[df_stat["stat_type"] == "월별"].dropna(subset=["month"])
chart2 = alt.Chart(month_df).mark_line(point=True).encode(
    x=alt.X("month:O", title="월", axis=alt.Axis(labelAngle=0)),
    y=alt.Y("count:Q", title="로드킬 수"),
    color="year:N",
    tooltip=["year", "month", "count"]
).properties(width=700, height=400)
st.altair_chart(chart2)

st.subheader("연도별 권역별 로드킬 수 통합 그래프")
region_df = df_stat[df_stat["stat_type"] == "권역별"].dropna(subset=["region"])
chart3 = alt.Chart(region_df).mark_bar().encode(
    x=alt.X("region:N", title="지역", sort='x', axis=alt.Axis(labelAngle=0)),
    y=alt.Y("count:Q", title="로드킬 수"),
    color="year:N",
    tooltip=["year", "region", "count"]
).properties(width=700, height=400)
st.altair_chart(chart3)

st.subheader("연도별 동물별 로드킬 수 통합 그래프")
a_df = df_stat[df_stat["stat_type"] == "종별"].dropna(subset=["animal"])
chart3 = alt.Chart(a_df).mark_bar().encode(
    x=alt.X("animal:N", title="동물", sort='x', axis=alt.Axis(labelAngle=0)),
    y=alt.Y("count:Q", title="로드킬 수"),
    color="year:N",
    tooltip=["year", "animal", "count"]
).properties(width=700, height=400)
st.altair_chart(chart3)

st.subheader(f"{selected_year}년 지역별 로드킬 발생 현황 (막대 그래프)")
region_df_filtered = df_stat[(df_stat["stat_type"] == "권역별") & (df_stat["year"] == selected_year)].dropna(subset=["region"])
chart_region = alt.Chart(region_df_filtered).mark_bar().encode(
    x=alt.X("region:N", title="지역", sort='x', axis=alt.Axis(labelAngle=0)),
    y=alt.Y("count:Q", title="로드킬 수"),
    color="year:N",
    tooltip=["year", "region", "count"]
).properties(width=700, height=400)
st.altair_chart(chart_region)

st.subheader(f"{selected_year}년 동물별 로드킬 수 (막대 그래프)")
animal_df_filtered = df_stat[(df_stat["stat_type"] == "종별") & (df_stat["year"] == selected_year)].dropna(subset=["animal"])
chart_animal = alt.Chart(animal_df_filtered).mark_bar().encode(
    x=alt.X("animal:N", title="동물", sort='x', axis=alt.Axis(labelAngle=0)),
    y=alt.Y("count:Q", title="로드킬 수"),
    color="year:N",
    tooltip=["year", "animal", "count"]
).properties(width=700, height=400)
st.altair_chart(chart_animal)

st.subheader(f"{selected_year}년 월별 로드킬 수 (막대 그래프)")
month_df_filtered = df_stat[(df_stat["stat_type"] == "월별") & (df_stat["year"] == selected_year)].dropna(subset=["month"])
chart_month = alt.Chart(month_df_filtered).mark_bar().encode(
    x=alt.X("month:N", title="월", sort='x', axis=alt.Axis(labelAngle=0)),
    y=alt.Y("count:Q", title="로드킬 수"),
    color="year:N",
    tooltip=["year", "month", "count"]
).properties(width=700, height=400)
st.altair_chart(chart_month)

st.subheader("종별 연도별 로드킬 누적 가로 막대그래프")
stack_df = df_stat[df_stat["stat_type"] == "종별"].dropna(subset=["animal", "year", "count"])
chart = alt.Chart(stack_df).mark_bar().encode(
    y=alt.Y("animal:N", title="동물"),
    x=alt.X("count:Q", title="로드킬 수", stack="zero"),
    color=alt.Color("year:N", title="연도"),
    tooltip=["animal", "year", "count"]
).properties(
    width=700,
    height=400,
    title="종별 연도별 로드킬 수"
)
st.altair_chart(chart) 