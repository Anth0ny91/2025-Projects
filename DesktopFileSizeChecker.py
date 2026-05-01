import os
import pathlib

# This works on both Mac and Windows automatically
desktop_dir = pathlib.Path.home() / "Desktop"
print(f'System path: {desktop_dir} \n')

total_size = 0
file_count = 0

for dirpath, dirnames, filenames in os.walk(desktop_dir):
    for file in filenames:
        # On Mac, some system files (like .DS_Store) can cause errors
        # This 'try' block prevents the script from crashing if it hits a restricted file
        try:
            full_path = os.path.join(dirpath, file)
            total_size += os.path.getsize(full_path)
            file_count += 1
        except (PermissionError, OSError):
            continue

# Bytes to KB and MB converter
kb_file_size = total_size / 1024
mb_file_size = total_size / (1024 * 1024)

# Output
print(f'Total size on Desktop: {kb_file_size:.2f} KB')
print(f'Total size on Desktop: {mb_file_size:.2f} MB')
print(f'Total file count: {file_count}')
