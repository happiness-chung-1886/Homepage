import markdown
import datetime

def convert_md_to_html(input_file):
    # 오늘 날짜 구하기 (예: 2026-05-23)
    today = datetime.date.today().strftime('%Y-%m-%d')
    output_file = f"source_{today}.html"
    
    # 마크다운 파일 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # HTML로 변환
    html = markdown.markdown(text)
    
    # HTML 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"변환이 완료되었습니다: {output_file}")

# 실행 예시
convert_md_to_html('Homepage/Archive for LinkedIn.md')