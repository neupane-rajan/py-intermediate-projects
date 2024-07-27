import os
import shutil
import datetime
import schedule
import time

source_dir = "file/location/which/file/you/want/tp/backup"
destination_dir = "From/where/you/want/to/put/your/backup file"


def backup(source, dest):
    today_date = datetime.date.today()
    dest_dir = os.path.join(dest, str(today_date))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("18:57").do(lambda: backup(source_dir, destination_dir))


while True:
    schedule.run_pending()
    time.sleep(60)
