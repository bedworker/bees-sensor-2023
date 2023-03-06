from datetime import datetime
import sys

# make an error handling function to broadcast to whatever system ends up working
def logger(e: str, level: int) -> None:
    # use actual logic when we figure out which service works
    if level == 1: # critical error
        print(f"(ERROR) {e}")
        sys.exit(1)
    if level == 2: # warning
        print(f"(WARN) {e}")
    if level == 3: # info
        print(f"(INFO) {e}")

def get_date_string(date: datetime = datetime.now()) -> str:
    return date.strftime("%y-%m-%d") # ex: 23-03-05