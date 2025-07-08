import os

folder = "my_folder"  # path to the folder with files

# loop through all files and rename them
for count, filename in enumerate(os.listdir(folder), 1):
    ext = os.path.splitext(filename)[1]  # get file extension
    new_name = f"file_{count}{ext}"      # generate new name
    os.rename(
        os.path.join(folder, filename),
        os.path.join(folder, new_name)
    )
