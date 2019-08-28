from SpeechDetector import SpeechDetector
from TextHandler import TextHandler
from GPIO_Handler import GPIO_Handler
from collections import deque
from multiprocessing import Process
from Threading import Thread

sd = SpeechDetector()
th = TextHandler()
# Initialize all display cells 0 - 13

word_que = deque(maxlen=10)
letter_que = deque()

GPIO.setmode(GPIO.BOARD)

if __name__ == "__main__":
    # Speech processing given process for heavier workload
    SpeechProcess = Process(target=sd.run())

    # Text processing thread initialization
    TextThread = Thread(target=th.run())

    # Boards initialized in threads, pins GPIO numbered
    cell0 = Thread(target=GPIO_Handler(0, 4))
    cell1 = Thread(target=GPIO_Handler(1, 17))
    cell2 = Thread(target=GPIO_Handler(2, 18))
    cell3 = Thread(target=GPIO_Handler(3, 27))
    cell4 = Thread(target=GPIO_Handler(4, 22))
    cell5 = Thread(target=GPIO_Handler(5, 23))
    cell6 = Thread(target=GPIO_Handler(6, 24))
    cell7 = Thread(target=GPIO_Handler(7, 25))
    cell8 = Thread(target=GPIO_Handler(8, 5))
    cell9 = Thread(target=GPIO_Handler(9, 6))
    cell10 = Thread(target=GPIO_Handler(10, 12))
    cell11 = Thread(target=GPIO_Handler(11, 13))
    cell2 = Thread(target=GPIO_Handler(12, 19))
    cell3 = Thread(target=GPIO_Handler(13, 16))
