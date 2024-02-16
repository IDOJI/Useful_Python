from concurrent.futures import ThreadPoolExecutor
import zipfile
import os
from threading import Lock

lock = Lock()

def zip_file(output_zipfile, root_dir, file):
    with lock:
        with zipfile.ZipFile(output_zipfile, 'a', zipfile.ZIP_DEFLATED) as zipf:
            try:
                zipf.write(os.path.join(root_dir, file), arcname=file)
            except Exception as e:
                print(f"Error zipping {file}: {e}")

def zip_folder(folder_path, output_zipfile, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for root_dir, dirs, files in os.walk(folder_path):
            for file in files:
                executor.submit(zip_file, output_zipfile, root_dir, file)




folder_name = "🌸Math_Linear Algebra(선형대수)"
folder_name = "Attachments"
folder_name = ".trash"
folder_name = ".obsidian"

folder_path = '/Users/Ido/Library/CloudStorage/GoogleDrive-yido.jee@gmail.com/내 드라이브/obsidian/SecondBrain_Obsidian/{}/'.format(folder_name)
output_zipfile = "/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/{}.zip".format(folder_name)  # 출력될 ZIP 파일 경로

# 폴더 압축 실행
zip_folder(folder_path, output_zipfile)
