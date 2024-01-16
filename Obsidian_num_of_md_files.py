import os

def count_markdown_files(path):
    """
    Count the number of markdown (.md) files in a given directory and its subdirectories.
    
    Parameters:
    path (str): The path to the directory to search in.
    
    Returns:
    int: The number of markdown files found.
    """
    md_count = 0
    # Walk through all directories and files in the path
    for root, dirs, files in os.walk(path):
      for file in files:
        # Check if the file is a markdonw file
        if file.endswith(".md"):
          md_count += 1
          
    return md_count

# Example usage:
# path = "your/directory/path"
# print(count_markdown_files(path))

# Note: Replace 'your/directory/path' with the actual path where you want to search for Markdown files.
