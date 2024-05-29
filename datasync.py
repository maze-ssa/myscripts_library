import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def initialize_sync(self):
        """Copy the source directory to the destination directory."""
        if os.path.exists(self.dst):
            shutil.rmtree(self.dst)
        shutil.copytree(self.src, self.dst)

    def on_modified(self, event):
        if not event.is_directory:
            self.sync_files_and_folders()

    def sync_files_and_folders(self):
        # Remove the destination path if it already exists
        if os.path.exists(self.dst):
            shutil.rmtree(self.dst)

        # Copy the source path to the destination path
        shutil.copytree(self.src, self.dst)

# Set the source and destination paths here
src = '/home/ubuntu/synology'
dst = '/home/ubuntu/fsx'

# Create the observer and handler
event_handler = FileChangeHandler(src, dst)
observer = Observer()

# Initialize the sync by copying the source directory to the destination directory
event_handler.initialize_sync()

# Schedule the observer to run in a separate thread
observer.schedule(event_handler, path=src, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()