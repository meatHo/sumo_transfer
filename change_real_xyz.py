try:
    import pandas as pd
    import sumolib

    # 1. 파일 읽기
    csv_file = 'single_vehicle_trace.csv'
    df = pd.read_csv(csv_file)

    # 2. SUMO 네트워크 파일 불러오기
    net_file = 'hats.net.xml'
    net = sumolib.net.readNet(net_file)

    # 3. 위도/경도 변환
    df[['lon', 'lat']] = df.apply(
        lambda row: net.convertXY2LonLat(row['x'], row['y']),
        axis=1,
        result_type='expand'
    )

    # 4. 저장
    df.to_csv('trace_with_latlon.csv', index=False)

    print("위도/경도 변환 완료! -> 'trace_with_latlon.csv' 파일 생성")

except Exception as e:
    print("에러 발생:", e)
