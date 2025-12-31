import pandas as pd
import requests
import json

# 1. 위도/경도가 포함된 CSV 파일 읽기
csv_file = 'trace_with_latlon.csv'
df = pd.read_csv(csv_file)

# 2. API 요청을 위한 데이터 준비
# Open-Elevation API는 한 번에 여러 위치를 조회할 수 있음
locations = {"locations": [{"latitude": row['lat'], "longitude": row['lon']} for index, row in df.iterrows()]}

# 3. API에 POST 요청 보내기
url = "https://api.open-elevation.com/api/v1/lookup"
headers = {'Content-type': 'application/json'}
response = requests.post(url, json=locations, headers=headers)

if response.status_code == 200:
    # 4. 응답(JSON)에서 고도 정보만 추출하여 새 열에 추가
    results = response.json()['results']
    elevations = [result['elevation'] for result in results]
    df['z'] = elevations

    # 5. 최종 3D 좌표가 포함된 CSV 파일 저장
    df.to_csv('final_3d_trace.csv', index=False)
    print("고도 정보 추가 완료! -> 'final_3d_trace.csv' 파일 생성")
else:
    print(f"API 요청 실패: {response.status_code}")