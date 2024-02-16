import os

def replace_filenames_string(path, old_string, new_string, recursive=True):
    # 현재 디렉토리의 모든 항목 가져오기
    entries = os.listdir(path)
    
    for entry in entries:
        full_path = os.path.join(path, entry)
        # 파일명 변경
        if os.path.isfile(full_path):
            if old_string in entry:
                new_entry = entry.replace(old_string, new_string)
                new_full_path = os.path.join(path, new_entry)
                os.rename(full_path, new_full_path)
                print(f"Renamed file: {entry} -> {new_entry}")
        # 디렉토리 내 파일명 변경 (재귀적으로)
        elif os.path.isdir(full_path) and recursive:
            replace_filenames_string(full_path, old_string, new_string)

# 테스트를 위한 예시 경로와 문자열
path = '/Users/Ido/Library/CloudStorage/GoogleDrive-yido.jee@gmail.com/내 드라이브/Obsidian/SecondBrain_Obsidian/🌸Stat_Bayesian(베이지안)/🟥Textbook/🟧데이터 분석을 위한 베이지안 통계 모델링(마츠우라)'
old_string = '🟪'
new_string = '🟧'

# 함수 호출
replace_filenames_string(path, old_string, new_string)
