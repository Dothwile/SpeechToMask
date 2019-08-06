import serial
import time
import Main
# from collections import deque


class TextHandler:

    # Packages text from SpeechDetector and communicates it to Teensy LC, (arduino if you nasty)

    def __init__(self):
        self.comm = serial.Serial("/dev/ttyACM0", 115200)

    def setup_comm(self):
        # Set up serial comm with MCU
        self.comm.open()
        handshake = False
        while not handshake:
            # Serial write a connection message
            self.comm.write('y')
            time.sleep(.5)
            # Serial Read for response
            if self.comm.available() != 0 and self.comm.read() is 'y':
                handshake = True
        print('Connection established')

    def text_packer(self):
        # Packs text for display on mask
        to_write_l1 = ""
        to_write_l2 = ""
        while len(to_write_l1) <= 7:
            cur_word = Main.word_que.pop(0)
            if len(cur_word) > 7 and len(to_write_l1) < 4:
                to_write_l1 = to_write_l1 + cur_word[0:2].capitalize() + ". "
            elif len(cur_word) < (7 - len(to_write_l1)):
                to_write_l1 = to_write_l1 + cur_word.capitalize() + " "
            else:
                to_write_l2 = cur_word.capitalize()
        while len(to_write_l2) <= 7:
            cur_word = Main.word_que.pop(0)
            if len(cur_word) > 7 and len(to_write_l2) < 4:
                to_write_l2 = to_write_l2 + cur_word[0:2] + ". "
            elif len(cur_word) < (7 - len(to_write_l2)):
                to_write_l2 = to_write_l2 + cur_word.capitalize() + " "
            else:
                Main.word_que.appendleft(cur_word)
                break
        full_write = (to_write_l1 + to_write_l2).ljust(14)

        self.comm.write(full_write.encode())

    def run(self):
        # Main run method
        while True:
            if len(Main.word_que) != 0 and len(Main.word_que) <= 10:
                self.text_packer()
                time.sleep(1)
            else:
                for x in range(0, 9):
                    Main.word_que.pop(0)

