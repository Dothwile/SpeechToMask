from SpeechDetector import SpeechDetector
from TextHandler import TextHandler
from GPIO_Handler import GPIO_Handler
from collections import deque
from multiprocessing import Process
from Threading import Thread

sd = SpeechDetector()
th = TextHandler()
gh = GPIO_Handler()

word_que = deque(maxlen=10)
letter_que = deque()

GPIO.setmode(GPIO.BOARD)

if __name__ == "__main__":
    SpeechProcess = Process(target=sd.run())