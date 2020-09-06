import time
import os
import shutil 
from watchdog.observers import Observer
from dotenv import load_dotenv
from watchdog.events import FileSystemEventHandler
load_dotenv()

folder_to_track = os.environ['TRACKED_FOLDER']
folder_dest = os.environ['HOME_FOLDER']

dest_subTypes = [('.pdf', '/documents'), ('.docx', '/documents'),
                ('.txt', '/documents'), ('.md', '/documents'),
                ('.csv', '/documents'), ('.xls', '/doucments'),
                ('.jpg', '/images'), ('.png', '/images'),
                ('.zip', '/packed'), ('.tar.xz', '/packages'),
                ('.deb', '/packages'), ('.tar.gz', '/packages'),
                ('.iso', '/packages')]


class FileHandler(FileSystemEventHandler): 
    i = 1
    for filename in os.listdir(folder_to_track):
        src = folder_to_track + "/" + filename
        for fileFormat, dest in dest_subTypes:
            if filename.endswith(fileFormat):
                newDestination = folder_dest + dest
                shutil.move(src, folder_dest + dest)


event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
