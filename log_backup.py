import os
import shutil
import zipfile

# Define the source and destination directories
source_dir = '/home/ubuntu/test/'
destination_dir = '/weekly_vm_config_config/'

# Check if the destination directory exists, and create it if it doesn't
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Define the zip file name with the current date
zip_filename = f'weekly_vm_config_{zipfile.ZipFile.nametime(time.gmtime())}.zip'

# Define the full path of the zip file
zip_path = os.path.join(destination_dir, zip_filename)

# Create a new zip file
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Walk through the source directory and copy all files to the zip file
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, arcname=os.path.relpath(file_path, source_dir))
#Finale Phase
print(f'Files copied to {destination_dir} and zipped as {zip_filename}')