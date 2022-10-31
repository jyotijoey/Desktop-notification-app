import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please take a break!!",
            message = "It is important for you to take short breaks in every twenty minutes.",
            timeout = 1
        )
        time.sleep(60*60)
