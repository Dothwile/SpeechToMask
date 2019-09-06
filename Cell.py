import Main
import RPIO.GPIO as GPIO
from switch import Switch



class Cell(object):

    def __init__(self, cell, data_pin):
        self.cell = cell
        self.pin = data_pin
        RPIO.setup(self.pin, RPIO.OUT)

    def shift_out(self):
        cur_let = Main.letter_que(self.cell)
        # Display letter checking in order from a English frequency table
        with Switch(cur_let) as case:
            if case("E"):
                # This is going to be a pain to implement
            if case("e"):
                # lower

            if case("T"):

            if case("t"):

            if case("A"):

            if case("a"):

            if case("O"):

            if case("o"):

            if case("I"):

            if case("i"):

            if case("N"):

            if case("n"):

            if case("S"):

            if case("s"):

            if case("R"):

            if case("r"):

            if case("H"):

            if case("h"):

            if case("D"):

            if case("d"):

            if case("L"):

            if case("l"):

            if case("U"):

            if case("u"):

            if case("C"):

            if case("c"):

            if case("M"):

            if case("m"):

            if case("F"):

            if case("f"):

            if case("Y"):

            if case("y"):

            if case("W"):

            if case("w"):

            if case("G"):

            if case("g"):

            if case("P"):

            if case("p"):

            if case("B"):

            if case("b"):

            if case("V"):

            if case("v"):

            if case("K"):

            if case("k"):

            if case("X"):

            if case("x"):

            if case("Q"):

            if case("q"):

            if case("J"):

            if case("j"):

            if case("Z"):

            if case("z"):

            else:
                print("placeholder")
