import os
import shutil
import zipfile
import datetime

def copy_and_zip():
    source_dir = "/home/ubuntu/test"
    dest_dir = "/weekly_vm_config_backup"

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the zip file name
    zip_filename = f"GB_PMX_VM_CONF_{current_datetime.strftime('%Y%m%d%H%M%S')}.zip"
    zip_path = os.path.join(dest_dir, zip_filename)

    # Zip the source directory
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(source_dir, "..")))

    print(f"Files zipped to {zip_path}")

#Finale
if __name__ == "__main__":
    copy_and_zip()