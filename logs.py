import const 
from datetime import datetime

def Debug(message: str):
    Base(message, 1)

def Info(message: str): 
    Base(message, 2)

def Core(message: str): 
    Base(message, 3)

def Base(message: str, emergency: int):
    if emergency == 1:
        label = "DEBUG"
    elif emergency == 2:
        label = "INFO"
    elif emergency == 3:
        label = "CORE"
    else:
        return

    if emergency >= const.LOGLEVEL:
        now = datetime.now()
        timeString = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f'[{label}] {timeString} - {message}')