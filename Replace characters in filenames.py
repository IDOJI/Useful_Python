import os
from pathlib import Path

def replace_emojis_in_names(root_path):
    
    for path, dirs, files in os.walk(root_path, topdown=False):
      
    
    
    
    :
        # 파일 이름 변경
        for name in files:
            new_name = name
            for old_emoji, new_emoji in emoji_map.items():
                new_name = new_name.replace(old_emoji, new_emoji)
            if new_name != name:
                os.rename(os.path.join(path, name), os.path.join(path, new_name))
        
        # 디렉토리 이름 변경
        for name in dirs:
            new_name = name
            for old_emoji, new_emoji in emoji_map.items():
                new_name = new_name.replace(old_emoji, new_emoji)
            if new_name != name:
                os.rename(os.path.join(path, name), os.path.join(path, new_name))

# 경로 설정
root_path = "/Users/Ido/Library/CloudStorage/GoogleDrive-yido.jee@gmail.com/내 드라이브/Obsidian/SecondBrain_Obsidian/🌸Stat_Bayesian(베이지안)/🟥Textbook/🟧데이터 분석을 위한 베이지안 통계 모델링(마츠우라)"

replace_emojis_in_names(root_path)
