from SpeechDetector import SpeechDetector
from TextHandler import TextHandler
from GPIO_Handler import GPIO_Handler
from collections import deque
from multiprocessing import Process
from Threading import Thread
from random import choice

sd = SpeechDetector()
th = TextHandler()
gp = GPIO_Handler()

word_que = deque(maxlen=10)
letter_que = deque(maxlen=70) # May tweak maxlen (cur assumes avg 7 let per word)

GPIO.setmode(GPIO.BOARD)

def start_up_msg():
    # Appends letter que with a rando startup message, since
    # letter que always at least 14 long no indexing errors
    start_msg = ('GIVE MEA BREAK',
                 'FUTURE IS HERE',
                 'ORA ORAORA ORA',
                 'TEARS  IN RAIN',
                 'POWER  REQUIEM',
                 '')

    letter_que.extend(choice(start_msg))

if __name__ == "__main__":
    choice(start_msg)
    # Speech processing given process for heavier workload
    SpeechProcess = Process(target=sd.run())
    # Text processing thread initialization
    TextThread = Thread(target=th.run())
    GpioThread = Thread(target=GPIO_Handler.run())
