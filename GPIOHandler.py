# imports here
from Cell import Cell


class GPIOHandler():

    def __init__(self):
        self.clock_pin = 0000 # TODO add actual clock pin number
        self.cell_list = {Cell(0, 4), Cell(1, 17),Cell(2, 18), Cell(3, 27),Cell(4, 22), Cell(5, 23),
                          Cell(6, 24), Cell(7, 25), Cell(8, 5), Cell(9, 6), Cell(10, 12), Cell(11, 13),
                          Cell(12, 19), Cell(13, 16)}

    @staticmethod
    def run(self):

        print("Gpio started")
