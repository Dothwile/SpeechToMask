import time
import Main
# from collections import deque


class TextHandler:

    # Packages text from SpeechDetector and communicates it to Teensy LC, (arduino if you nasty)

    def __init__(self):
        self.ALL_CAPS = False


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

        # TODO, in airport, when have Stack Exchange find the elegant cast from String to Byte Array
        for c in full_write:
            Main.letter_que.append(c)

    def run(self):
        # Main run method
        while True:
            if len(Main.word_que) != 0 and len(Main.word_que) <= 10:
                self.text_packer()
                time.sleep(1)
            elif len(Main.word_que) != 0:
                for x in range(0, 9):
                    Main.word_que.pop(0)

