from SpeechDetector import SpeechDetector
from TextHandler import TextHandler
from GPIO_Handler import GPIO_Handler
from collections import deque
from multiprocessing import Process
from Threading import Thread

sd = SpeechDetector()
th = TextHandler()
gh = GPIO_Handler()

word_que = deque()
letter_que = deque()

GPIO.setmode(GPIO.BOARD)

if __name__ == "__main__":
    p1 = Process(target=th.run())
    p2 = Process(target=sd.run())
    p3 = Thread(target=gh.run())
    p1.start()
    p2.start()
    p3.start()
