import xml.etree.ElementTree as ET
import csv

# 입력 파일과 출력 파일 이름 설정
xml_file = 'fcd.xml'
csv_file = 'single_vehicle_trace.csv'

# CSV 파일 생성 시작
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    # CSV 파일의 첫 줄(헤더) 작성
    writer.writerow(['time', 'vehicle_id', 'x', 'y', 'speed'])

    # XML 데이터 파싱
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 모든 시간대(timestep)의 데이터를 한 줄씩 읽어서 CSV로 쓰기
    for timestep in root.findall('timestep'):
        time = timestep.get('time')
        for vehicle in timestep.findall('vehicle'):
            writer.writerow([
                time,
                vehicle.get('id'),
                vehicle.get('x'),
                vehicle.get('y'),
                vehicle.get('speed')
            ])

print(f"변환 완료! -> '{csv_file}' 파일이 생성되었습니다.")