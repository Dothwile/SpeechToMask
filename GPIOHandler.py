import Main
import RPIO.GPIO as GPIO
from switch import Switch



class GPIOHandler(object):

    def __init__(self, cell, datapin):
        self.cell = cell
        self.pin = datapin

    # Oh no...

    def run(self):
        cur_let = Main.letter_que(self.cell)
        # This is not going to fun...
        with Switch(cur_let) as case:
            case("E")



