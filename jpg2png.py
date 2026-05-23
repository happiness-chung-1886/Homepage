import os
from PIL import Image

def convert_jpg_to_png(folder="images"):
    # 폴더 내의 모든 파일을 확인
    for filename in os.listdir(folder):
        if filename.lower().endswith(".jpg"):
            # 파일 경로 설정
            jpg_path = os.path.join(folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(folder, png_filename)
            
            # 이미지 열기 및 저장
            with Image.open(jpg_path) as img:
                img.save(png_path, "PNG")
                print(f"변환 완료: {filename} -> {png_filename}")

# 실행
convert_jpg_to_png()