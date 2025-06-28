import os
import pathlib

#For checking the sizes of folders, files, etc.
desktop_dir = pathlib.Path.home() / "Desktop"
print(f'Windows path: {desktop_dir} \n')

#Define
total_size = 0
file_count = 0

#Checks the size of dirpath into bytes
for dirpath, dirnames, filenames in os.walk(desktop_dir):
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        total_size += os.path.getsize(full_path)
        file_count += 1

#Bytes to KB and MB converter
kb_file_size = total_size / 1024
mb_file_size = total_size / 1024 / 1024

#Output
print(f'Total size of files in KB: {kb_file_size:.2f} KB')
print(f'Total size of files in MB: {mb_file_size:.2f} MB')

#File counter
print(f'file count: {file_count}')



