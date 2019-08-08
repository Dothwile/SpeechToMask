import Main
import RPIO.GPIO as GPIO
import time


class GPIOHandler(object):

    def __init__(self, cell, pin, oe):
        self.cell = cell
        self.pin = pin
        self.oe = oe

    # Oh no...

    def run(self):

        # Find scan for top section of letter
        if Main.letter_que(self.cell) == ' ':
            for i in range(0, 7):
                # Write low
                # Clock
        elif Main.letter_que(self.cell) in {''}:

        elif Main.letter_que(self.cell) in {''}:

        elif Main.letter_que(self.cell) in {''}: