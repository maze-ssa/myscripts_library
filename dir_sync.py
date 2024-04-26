import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirectorySyncHandler(FileSystemEventHandler):
    def __init__(self, src_dir, dest_dir):
        self.src_dir = src_dir
        self.dest_dir = dest_dir

    def on_modified(self, event):
        if not event.is_directory:
            src_file = event.src_path
            rel_path = os.path.relpath(src_file, self.src_dir)
            dest_file = os.path.join(self.dest_dir, rel_path)

            # Create destination directory if it doesn't exist
            dest_dir = os.path.dirname(dest_file)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Copy the file to the destination directory
            shutil.copy2(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

def sync_directories(src_dir, dest_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Initialize the watchdog observer
    event_handler = DirectorySyncHandler(src_dir, dest_dir)
    observer = Observer()
    observer.schedule(event_handler, src_dir, recursive=True)
    observer.start()

    # Keep the observer running until you stop it
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    src_dir = "/home/adm-ssa/synology_nfs"
    dest_dir = "/home/adm-ssa/aws_nfs"
    sync_directories(src_dir, dest_dir)
