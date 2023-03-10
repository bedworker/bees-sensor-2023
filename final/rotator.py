# called every day at 0100

import os
import subprocess
from datetime import datetime, timedelta
from common import logger, get_date_string

directory = os.path.dirname(os.path.abspath(__file__))

today_string = get_date_string(datetime.today())
todaylog_exists = os.path.exists(f"{directory}/data/{today_string}.log")
yesterday = datetime.today() - timedelta(days=1)
yesterday_string = get_date_string(yesterday)
yesterlog_exists = os.path.exists(f"{directory}/data/{yesterday_string}.log")
yesteryesterday = datetime.today() - timedelta(days=2)
yesteryesterday_string = get_date_string(yesteryesterday)
yesteryesterlog_exists = os.path.exists(f"{directory}/data/{yesteryesterday_string}.log")

if not todaylog_exists:
    logger(f"Today's log {today_string}.log does not exist!", 1)
if yesterlog_exists:
    subprocess.run(["rclone", "copyto", f"/home/bees/Documents/final/data/{yesterday_string}.log", f"bee2:liambeedata/data/{yesterday_string}.log"])
    # os.system(f"rclone copyto /home/bees/Documents/final/data/{yesterday_string}.log bee2:liambeedata/data/{yesterday_string}.log")

    try:
        os.remove(f"{directory}/data/{yesteryesterday_string}.log")
        logger(f"Yesteryesterday's log ({yesteryesterday_string}.log) has been successfully deleted.", 3) 
    except FileNotFoundError:
        logger(f"Yesteryesterday's log ({yesteryesterday_string}.log) does not exist.", 2)

else:
    logger("Yesterlog does not exist!", 1)