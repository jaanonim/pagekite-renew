import json
import os
import threading
import time
from datetime import datetime, timedelta

import schedule

file_name = "settings.json"


def startTread():
    thread = threading.Thread(target=check, name="schedule")
    thread.start()


def check():
    s = loadData()
    if s:
        time = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")
        if time > datetime.now():
            return
    saveData()
    run()


def run():
    from main import main

    main()


def saveData():
    time = datetime.now() + timedelta(days=29)
    with open(file_name, "w") as json_file:
        json.dump({"time": str(time)}, json_file)


def loadData():
    try:
        f = open(file_name)
        data = json.load(f)
        time = data["time"]
        f.close()
        return time
    except Exception as e:
        return None


def mainL():
    schedule.every().day.do(startTread)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    mainL()
