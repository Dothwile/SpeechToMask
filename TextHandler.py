import serial
import time
import Main
from collections import deque

class TextHandler:

    # Packages text from SpeechDetector and communicates it to arduino

    def __init__(self):
        self.comm = serial.Serial("/dev/ttyACM0", 9600)


    def setup_comm(self):
        # Set up serial comm with MCU
    handshake = False
    while not handshake:
        # Serial write a connection message
        time.sleep(100)
        # Serial Read for response
        if True:
            handshake = True

    def text_packer(self):
        # Packs text for display on mask
        cur_chars_l1 = 0
        cur_chars_l2 = 0
        to_write_l1 = ""
        to_write_l2 = ""
        



        


    def run(self):
        # Main run method
        while True:
            if len(Main.word_que) != 0:
                self.text_packer()
