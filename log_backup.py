import os
import shutil
import datetime
import zipfile

# Define source and destination directories
source_dir = '/home/ubuntu/test/'
destination_dir = '/weekly_vm_config_config/'

# Check if destination directory exists, and create it if it doesn't
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Copy all files from source to destination
for root, dirs, files in os.walk(source_dir):
    for file in files:
        src_file_path = os.path.join(root, file)
        dst_file_path = os.path.join(destination_dir, file)
        shutil.copy(src_file_path, dst_file_path)

# Zip the copied files
zip_filename = 'vm_config_' + datetime.datetime.now().strftime('%Y%m%d') + '.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(destination_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path)

print('Files copied and zipped successfully!')