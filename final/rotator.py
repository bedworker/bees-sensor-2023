# called every day at 0100

import os
from datetime import datetime, timedelta
from common import logger, get_date_string

directory = os.path.dirname(os.path.abspath(__file__))

yesterday = datetime.today() - timedelta(days=1)
yesterday_string = get_date_string(yesterday)
yesterlog_exists = os.path.exists(f"{directory}/data/{yesterday_string}.log")
yesteryesterday = datetime.today() - timedelta(days=2)
yesteryesterday_string = get_date_string(yesteryesterday)
yesteryesterlog_exists = os.path.exists(f"{directory}/data/{yesteryesterday_string}.log")


if yesterlog_exists:
    os.system(f"rclone copyto /home/bees/Documents/final/data/{yesterday_string}.log bee2:liambeedata/data/{yesterday_string}.log")

    try:
        os.remove(f"{directory}/data/{yesteryesterday_string}.log")
        logger(f"Yesteryesterday's log ({yesteryesterday_string}.log) has been successfully deleted.", 3) 
    except FileNotFoundError:
        logger(f"Yesteryesterday's log ({yesteryesterday_string}.log) does not exist.", 2)

else:
    logger("Yesterlog does not exist!", 1)