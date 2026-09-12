import os
import shutil
import threading
import time
from datetime import datetime
import schedule

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "backup_source")
DEST_DIR = os.path.join(BASE_DIR, "backup_destination")


def backup_job():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(DEST_DIR, f"backup_{timestamp}")
    os.makedirs(backup_folder, exist_ok=True)

    """
    The next loop walks through every file in the source folder,
    builds the full path to each file,
    builds the full path to where the file should go,
    and copies it.
    """

    for filename in os.listdir(SOURCE_DIR):
        src_path = os.path.join(SOURCE_DIR, filename)
        dst_path = os.path.join(backup_folder, filename)
        shutil.copy2(src_path, dst_path)

    print(f"Backup completed at {timestamp}")


def threaded_backup_job():
    thread = threading.Thread(target=backup_job)
    thread.start()


schedule.every(10).seconds.do(threaded_backup_job)

while True:
    schedule.run_pending()
    time.sleep(1)
