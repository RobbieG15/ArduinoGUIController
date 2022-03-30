from pyfirmata import *
import ast
from dataCollectionStorage import boardTypes

class RunPreset:
    def __init__(self):
        self.board = ''
        self.port = ''
        self.pins = []
        global board
        global pins
        pins = []

    def importPreset(self, presetName):
        with open('presets.txt') as presets:
            lines = presets.read().splitlines()
            for i, line in enumerate(lines):
                if line == presetName:
                    self.board = lines[i+1]
                    self.port = lines[i+2]
                    self.pins = ast.literal_eval(lines[i+3])
                    break

    def connectBoard(self): 
        global board
        try:
            if self.board == boardTypes[0]:
                board = Arduino(self.port)
            elif self.board == boardTypes[1]:
                board = ArduinoMega(self.port)
            elif self.board == boardTypes[2]:
                board = ArduinoDue(self.port)
            elif self.board == boardTypes[3]:
                board = ArduinoNano(self.port)
            else:
                # TODO: need to handle this case 
                # return to main menu and flash message
                print('Invalid Board. Create new or select different preset.')
        except Exception:
            # TODO: need to handle this case
            # return to main menu, flash message
            print('Cannot connect to the board on this port.')
            print('Try making a new preset and checking what port and specific board you are using.')

    def establishPinConnection(self):
        global pins
        for pin in self.pins:
            try:
                if pin[3] == 's':
                    pin = board.get_pin(f'{pin[1]}:{pin[2]}:o')
                    pin.mode = SERVO
                else:
                    pin = board.get_pin(f'{pin[1]}:{pin[2]}:{pin[3]}')
                    if pin[3] == 'p':
                        pin.mode = PWM
                    elif pin[3] == 'o':
                        pin.mode = OUTPUT
                    else:
                        pin.mode = INPUT
                print(f'Established connection to pin {pin[2]}.')
            except Exception:
                # TODO: need to handle this case
                # return to main menu and flash message
                print(f'Cannot connect to pin {pin[2]}.')
                print('Make a new preset or switch your connections around to the board.')

