import os
import re

def convert_md_links(md_file_path, variables_file_path):
    # 1. variables.md에서 {image1: images/image1.png} 형태의 딕셔너리 생성
    mapping = {}
    with open(variables_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # [image1]: images/image1.png 형태를 찾음
        matches = re.findall(r'\[(image\d+)\]:\s*(images/image\d+\.png)', content)
        for key, path in matches:
            mapping[key] = path

    # 2. 마크다운 파일 내용 읽기
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 3. [][image1] 형태를 찾아서 ![](images/image1.png)로 변환
    def replace_link(match):
        img_id = match.group(1) # image1 추출
        if img_id in mapping:
            return f"![]({mapping[img_id]})"
        return match.group(0) # 매칭되는 게 없으면 그대로 둠

    new_content = re.sub(r'\[\]\[(image\d+)\]', replace_link, md_content)

    # 4. 결과 저장
    with open(md_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"변환 완료: {md_file_path}")

# 사용법: mds 폴더 안의 파일들과 variables.md 경로 설정
mds_folder = '2026-05-24/mds'
var_file = 'images/variables.md' # 본인 환경에 맞게 수정하세요

for filename in os.listdir(mds_folder):
    if filename.endswith(".md"):
        convert_md_links(os.path.join(mds_folder, filename), var_file)