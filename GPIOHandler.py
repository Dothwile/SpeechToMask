import Main
import RPIO.GPIO as GPIO



class GPIOHandler(object):

    def __init__(self, cell, pin):
        self.cell = cell
        self.pin = pin

    # Oh no...


    def run(self):
        cur_let = Main.letter_que(self.cell)


