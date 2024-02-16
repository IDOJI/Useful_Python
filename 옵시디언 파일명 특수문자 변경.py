import os

def replace_special_characters(directory, special_characters):
    # Convert directory to an absolute path (optional, for convenience)
    directory = os.path.abspath(directory)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        # Combine directories and files for processing
        all_items = dirs + files
        for item in all_items:
            # Check if item contains any of the special characters
            if any(char in item for char in special_characters):
                # Replace each special character with a star
                new_name = item
                for char in special_characters:
                    new_name = new_name.replace(char, '⭐')
                old_path = os.path.join(root, item)
                new_path = os.path.join(root, new_name)
                # Rename the item
                os.rename(old_path, new_path)
                print(f'Renamed "{old_path}" to "{new_path}"')

# Example usage
directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian'
directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian/⭐️Stat_Bayesian(베이지안)'
directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian/⭐CS_AI_Machine Learning'
directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian/⭐CS_Lang_R'
directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian/❎Stat_Regression Analysis(회귀분석)'
directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian/⛅CS_Lang_R/⭐MyFunction'
special_characters = ['🟪', '🟥', '🌍', '🟦', '🟨', '💚', '🔳', '🟧', '💙', '🌸', '🟩', '💜']  # List the special characters you want to replace
replace_special_characters(directory, special_characters)
