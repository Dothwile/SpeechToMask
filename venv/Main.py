from SpeechDetector import SpeechDetector
from TextHandler import TextHandler
from collections import deque

sd = SpeechDetector()
th = TextHandler()

word_que = deque() # Needs testing to see if max length should be added

if __name__ == "__main__":
    th.setup_comm()
    th.run()
    sd.run()