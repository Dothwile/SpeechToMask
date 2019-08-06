from SpeechDetector import SpeechDetector
from TextHandler import TextHandler
from collections import deque
from multiprocessing import Process

sd = SpeechDetector()
th = TextHandler()

word_que = deque()

if __name__ == "__main__":
    th.setup_comm()
    p1 = Process(target=th.run())
    p2 = Process(target=sd.run())
    p1.start()
    p2.start()