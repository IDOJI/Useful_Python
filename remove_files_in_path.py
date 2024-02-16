import os

def delete_files(file_paths):
    for path in file_paths:
        try:
            os.remove(path)
            print(f"Deleted: {path}")
        except OSError as e:
            print(f"Error deleting {path}: {e.strerror}")

# Example usage
file_paths = [
    '/path/to/your/file1.txt',
    '/path/to/your/file2.txt',
    # Add more file paths as needed
]

delete_files(file_paths)
