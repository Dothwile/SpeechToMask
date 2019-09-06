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
# Initialize all display cells 0 - 13

word_que = deque(maxlen=10)
letter_que = deque()

# Oh this is a hack...
# Nvm Im an idiot

def start_up_msg():
    start_msg = ('GIVE MEA BREAK',
                 'FUTURE IS HERE',
                 'ORA ORAORA ORA',
                 'TEARS  IN RAIN')

    letter_que.extend(choice(start_msg))

GPIO.setmode(GPIO.BOARD)

if __name__ == "__main__":
    # Speech processing given process for heavier workload
    SpeechProcess = Process(target=sd.run())

    # Text processing thread initialization
    TextThread = Thread(target=th.run())
    GpioThread = Thread(target=gp.run())
    choice(start_msg)

    # Boards initialized in threads, pins GPIO numbered
    # KISS always
