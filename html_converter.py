import os
import datetime
import markdown

def convert_md_to_html(input_file):
    # 오늘 날짜 구하기 (예: 2026-05-23)
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    # 1. 날짜 이름으로 된 폴더가 없으면 생성
    if not os.path.exists(today):
        os.makedirs(today)
    
    # 2. 폴더 경로와 파일 이름을 합쳐서 저장 경로 지정
    output_file = os.path.join(today, f"additional_inf_{today}.html")
    
    # 마크다운 파일 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # HTML로 변환
    html = markdown.markdown(text)
    
    # HTML 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"변환 완료! 파일 위치: {output_file}")

# 실행 예시
convert_md_to_html('additional_info.md')