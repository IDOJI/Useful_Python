import os

def find_ds_store_files(directory):
    ds_store_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ".DS_Store":
                ds_store_files.append(os.path.join(root, file))
    return ds_store_files



directory = '/Users/Ido/Library/CloudStorage/Dropbox/GitHub/Github___Obsidian/Obsidian'  # Replace this with your target directory
ds_store_files = find_ds_store_files(directory)
print("\n".join(ds_store_files))


 
# remove files
delete_files(ds_store_files)
