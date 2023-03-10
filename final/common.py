from datetime import datetime
import subprocess
import sys
import os

GOTIFY_TOKEN = "ASzE51ToVVutxs1"
GOTIFY_ADDRESS = "http://167.248.85.93:8335"

GOTIFY_DEFUALT_TITLE = "Bee Sensor"
GOTIFY_DEFAULT_MESSAGE = "Something went wrong!"

# make an error handling function to broadcast to whatever system ends up working
def logger(e: str, level: int) -> None:
    message = GOTIFY_DEFAULT_MESSAGE
    title = GOTIFY_DEFUALT_TITLE

    # priority:
    # 0, 1, 2, 3: completely silent
    # 4, 5, 6: silent notification, vibrates

    prefix = ""
    if e:
        message = e
        
    if level == 1: # critical error
        prefix = "(ERROR)"
        priority = 10
        # sys.exit(1)
    if level == 2: # warning
        prefix = "(WARN)"
        priority = 5
    if level == 3: # info
        prefix = "(INFO)"
        priority = 0
    
    subprocess.run(["curl", f"{GOTIFY_ADDRESS}/message?token={GOTIFY_TOKEN}", "-F", f"\"title={title}\"", "-F", f"message=\"{prefix} {message}\"", "-F", f"priority={priority}"])
    # os.system(f"curl \"{GOTIFY_ADDRESS}/message?token={GOTIFY_TOKEN}\" -F \"title={title}\" -F \"message={prefix} {message}\" -F \"priority={priority}\"")

    if level == 1: sys.exit(1)

def get_date_string(date: datetime = datetime.now()) -> str:
    return date.strftime("%y-%m-%d") # ex: 23-03-05