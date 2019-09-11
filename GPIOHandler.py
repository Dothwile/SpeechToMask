from Cell import Cell
import RPIO.GPIO as GPIO


class GPIOHandler:

    def __init__(self):
        self.clck_pin = 7
        self.rclk_pin = 0000
        self.cell_list = {Cell(0, 4), Cell(1, 17), Cell(2, 18), Cell(3, 27),Cell(4, 22), Cell(5, 23),
                          Cell(6, 24), Cell(7, 25), Cell(8, 5), Cell(9, 6), Cell(10, 12), Cell(11, 13),
                          Cell(12, 19), Cell(13, 16)}
        self.cur_row = 0
        self.cur_col = 0
        RPIO.setup(self.clck_pin, RPIO.OUT)

    def run(self):
        print("Gpio started")
        for cell in self.cell_list:
            cell.letter_map[cell.cur_let]()
        RPIO.output(self.clck_pin, True)
        # ~60ns pulse for clock, sleep is too long, could add up to stutter
        RPIO.output(self.clck_pin, False)

        self.cur_row += 1
        if self.cur_row == 9:
            self.cur_row = 0
            self.cur_col += 1
            RPIO.output(self.rclk_pin, True)
            RPIO.output(self.rclk_pin, False)
        if self.cur_col == 3:
            self.cur_col = 0
