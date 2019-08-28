import time
import Main
# from collections import deque


class TextHandler:

    # Packages text from SpeechDetector and communicates it to Teensy LC, (arduino if you nasty)

    def __init__(self):
        self.ALL_CAPS = False
        self.L337 = False


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

        if self.ALL_CAPS:
            full_write = full_write.upper()

        if self.L337:
            full_write = full_write.replace("S", "$")
            full_write = full_write.replace("s", "$")
            full_write = full_write.replace("T", "7")
            full_write = full_write.replace("t", "7")
            full_write = full_write.replace("A", "4")
            full_write = full_write.replace("G", "6")
            # Here I ask myself again... why?

        # TODO, in airport, when have Stack Exchange find the elegant cast from String to Byte Array
        for c in full_write:
            Main.letter_que.append(c)

    def run(self):
        # Main run method
        while True:
            # Body
            self.text_packer()
