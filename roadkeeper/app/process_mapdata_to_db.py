import streamlit as st
import pandas as pd
import mysql.connector
import os
import chardet

# MySQL 연결
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456", # 필요에 따라 비밀번호를 수정하세요
        database="roadkill_db",
        auth_plugin="caching_sha2_password"
    )

# reverse 매핑 (사용자가 원하는 컬럼명 영어 변환)
reverse_column_mapping = {
    'source': ['출처', 'Source'],
    'date': ['발생일', 'Date'],
    'location': ['위치정보', 'Location', '구간', '주소', '지역', '구간명', '위치명'],
    'animal_name': ['동물명', 'Animal'],
    'latitude': ['위도', 'lat', 'Latitude'],
    'longitude': ['경도', 'lon', 'Longitude'],
    'additional_info': ['추가정보', 'Description', '비고', '세부위치']
}

def find_column(df, candidates):
    for col in df.columns:
        for candidate in candidates:
            if candidate in col:
                return col
    return None

def rename_columns_to_english(df):
    mapped = {}
    for eng_col, kor_candidates in reverse_column_mapping.items():
        col_name = find_column(df, kor_candidates)
        if col_name:
            mapped[col_name] = eng_col
    return df.rename(columns=mapped)

def insert_dataframe_to_db(df):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO roadkill_map (
            source, date, location, animal_name, latitude, longitude, additional_info
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    success_count = 0
    skip_count = 0

    for _, row in df.iterrows():
        # 필수값 체크 (latitude, longitude는 필수)
        if pd.isna(row.get('latitude')) or pd.isna(row.get('longitude')):
            skip_count += 1
            continue

        values = tuple(row.get(col) if pd.notna(row.get(col)) else None for col in
                       ['source', 'date', 'location', 'animal_name', 'latitude', 'longitude', 'additional_info'])

        try:
            cursor.execute(insert_query, values)
            success_count += 1
        except Exception as e:
            # 오류 발생 시 건너뛰고 메시지 출력
            print(f"데이터 삽입 오류: {e}, 데이터: {values}")
            skip_count += 1

    conn.commit()
    cursor.close()
    conn.close()
    return success_count, skip_count


def main():
    st.title("로드킬 지도 데이터 처리 및 DB 삽입")
    st.write("아래 버튼을 클릭하면 'mapdata' 폴더의 지정된 CSV 파일들을 읽어 데이터베이스에 삽입합니다.")

    csv_files = [
        "mapdata/2023_roadkill.csv",
        "mapdata/2024_ulsan_roadkill.csv",
        "mapdata/2023_sokrisan_roadkill.csv",
        "mapdata/2023_nationalpark_roadkill.csv",
        "mapdata/2024_nationalpark_roadkill.csv"
    ]

    if st.button("CSV 파일 처리 시작"):
        st.info("CSV 파일 처리를 시작합니다...")
        
        total_success = 0
        total_skip = 0

        existing_files = [f for f in csv_files if os.path.exists(f)]

        if not existing_files:
            st.warning("처리할 CSV 파일을 찾을 수 없습니다. 'mapdata' 폴더와 파일 경로를 확인해주세요.")
            return
            
        st.write(f"처리할 파일 수: {len(existing_files)}")

        for file_path in existing_files:
            try:
                st.write(f"\n처리 중인 파일: {os.path.basename(file_path)}")

                # 파일 인코딩 감지
                with open(file_path, 'rb') as f:
                    enc = chardet.detect(f.read())['encoding']
                st.write(f"파일 인코딩: {enc}")

                # CSV 파일 읽기
                df = pd.read_csv(file_path, encoding=enc)
                st.write(f"총 {len(df)}개의 행을 읽었습니다.")

                # 컬럼 영어명으로 변경
                df = rename_columns_to_english(df)

                # 컬럼 부족한 경우 채우기
                for col in reverse_column_mapping.keys():
                    if col not in df.columns:
                        df[col] = None

                # 위도, 경도 숫자형 변환
                df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
                df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
                
                # DB 삽입
                success, skip = insert_dataframe_to_db(df)
                total_success += success
                total_skip += skip

                st.write(f"성공: {success}건, 건너뜀: {skip}건")

            except Exception as e:
                st.error(f"파일 처리 중 오류 발생 ({os.path.basename(file_path)}): {str(e)}")

        st.success("=== 처리 완료 ===")
        st.write(f"전체 성공: {total_success}건")
        st.write(f"전체 건너뜀: {total_skip}건")

if __name__ == '__main__':
    main() 