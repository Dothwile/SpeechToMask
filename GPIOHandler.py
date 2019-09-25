from Cell import Cell
from time import sleep
import RPIO.GPIO as GPIO


class GPIOHandler:
    clck_pin = 7
    rclk_pin = 0000
    cell_list = {Cell(0, 4), Cell(1, 17), Cell(2, 18), Cell(3, 27), Cell(4, 22), Cell(5, 23),
                 Cell(6, 24), Cell(7, 25), Cell(8, 5), Cell(9, 6), Cell(10, 12), Cell(11, 13),
                 Cell(12, 19), Cell(13, 16)}
    cur_row = 0
    cur_col = 0
    RPIO.setup(self.clck_pin, RPIO.OUT)

    def run(self):
        print("Gpio started")
        for cell in self.cell_list:
            cell.letter_map[cell.cur_let]()
        RPIO.output(self.clck_pin, True)
        sleep(.001)
        # ~60ns pulse for clock, sleep is too long, could add up to stutter
        RPIO.output(self.clck_pin, False)
        GPIOHandler.cur_row += 1
        if GPIOHandler.cur_row == 9:
            GPIOHandler.cur_row = 0
            GPIOHandler.cur_col += 1
            RPIO.output(self.rclk_pin, True)
            sleep(.001)
            RPIO.output(self.rclk_pin, False)
        if GPIOHandler.cur_col == 3:
            cur_col = 0
            for cell in cell_list:
                cell.new_let()
