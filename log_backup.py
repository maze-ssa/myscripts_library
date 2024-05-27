import os
import shutil
import zipfile

def copy_and_zip():
    source_dir = "/home/ubuntu/test"
    dest_dir = "/weekly_vm_config_backup"

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy all files and zips from source to destination
    for item in os.listdir(source_dir):
        src = os.path.join(source_dir, item)
        dst = os.path.join(dest_dir, item)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
        elif os.path.isdir(src):
            shutil.copytree(src, dst)

    # Zip the destination directory
    zip_filename = f"{dest_dir}_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + ".zip"
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(dest_dir):
            for file in files:
                zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(dest_dir, "..")))

    print(f"Files copied and zipped to {zip_filename}")

if __name__ == "__main__":
    copy_and_zip()