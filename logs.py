import const 
import datetime

def Debug(message: string):
    Base(message, 1)

def Info(message: string): 
    Base(message, 2)

def Core(message: string): 
    Base(message, 3)

def Base(message: string, emergency: int):
    if emergency == 1:
        message = "DEBUG"
    elif emergency == 2:
        message = "INFO"
    elif emergency == 3:
        message = "CORE"
    else:
        return

    if emergency >= const.LOGLEVEL:
        now = datetime.now()
        timeString = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f'[{message}] {timeString} - {message}')