import serial
import SpeechDetector

class TextHandler:

    # Packages text from SpeechDetector and communicates it to arduino

    def __init__(self):
        self.comm = serial.Serial("/dev/ttyACM0", 9600)

    def setup_comm(self):

    def text_packer(self, ):
