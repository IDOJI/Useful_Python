import os

def find_invalid_file_names(root_path):
    # 윈도우에서 사용할 수 없는 문자 목록
    invalid_chars = set('<>:\"/\\|?*')
    
    # root_path부터 시작하여 모든 디렉토리와 파일을 순회
    for root, dirs, files in os.walk(root_path):
        # 모든 디렉토리에 대해
        for dir_name in dirs:
            # 디렉토리 이름에 유효하지 않은 문자가 있는지 확인
            if any(char in dir_name for char in invalid_chars):
                print(f"Invalid directory name: {os.path.join(root, dir_name)}")
        
        # 모든 파일에 대해
        for file_name in files:
            # 파일 이름에 유효하지 않은 문자가 있는지 확인
            if any(char in file_name for char in invalid_chars):
                print(f"Invalid file name: {os.path.join(root, file_name)}")

# 사용 예시:
find_invalid_file_names("/Users/Ido/Library/CloudStorage/GoogleDrive-yido.jee@gmail.com/내 드라이브/Obsidian/SecondBrain_Obsidian")
