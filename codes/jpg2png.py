import os
from PIL import Image

def convert_jpg_to_png(folder="images"):
    # 폴더가 존재하는지 먼저 확인
    if not os.path.exists(folder):
        print(f"오류: '{folder}' 폴더를 찾을 수 없습니다.")
        return

    for filename in os.listdir(folder):
        # jpg와 jpeg 모두 확인
        if filename.lower().endswith((".jpg", ".jpeg")):
            jpg_path = os.path.join(folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(folder, png_filename)
            
            try:
                with Image.open(jpg_path) as img:
                    img.save(png_path, "PNG")
                    print(f"성공: {filename} -> {png_filename}")
            except Exception as e:
                print(f"실패: {filename} - 오류 내용: {e}")

# 실행
convert_jpg_to_png()