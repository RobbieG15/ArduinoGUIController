from pyfirmata import *
import ast
from dataCollectionStorage import boardTypes
import keyboard

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
                print(f'Established connection to {self.board} on port {self.port}.')
            elif self.board == boardTypes[1]:
                board = ArduinoMega(self.port)
                print(f'Established connection to {self.board} on port {self.port}.')
            elif self.board == boardTypes[2]:
                board = ArduinoDue(self.port)
                print(f'Established connection to {self.board} on port {self.port}.')
            elif self.board == boardTypes[3]:
                board = ArduinoNano(self.port)
                print(f'Established connection to {self.board} on port {self.port}.')
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
        for i, pin in enumerate(self.pins):
            try:
                if pin[3] == 's':
                    pins.append(board.get_pin(f'{pin[1]}:{pin[2]}:o'))
                    pins[i].mode = SERVO
                else:
                    pins.append(board.get_pin(f'{pin[1]}:{pin[2]}:{pin[3]}'))
                    if pin[3] == 'p':
                        pin[i].mode = PWM
                    elif pin[3] == 'o':
                        pins[i].mode = OUTPUT
                    else:
                        pins[i].mode = INPUT
                print(f'Established connection to pin {pin[2]}.')
            except Exception:
                # TODO: need to handle this case
                # return to main menu and flash message
                print(f'Cannot connect to pin {pin[2]}.')
                print('Make a new preset or switch your connections around to the board.')

    def operatePreset(self):
        global pins
        global board

        it = pyfirmata.util.Iterator(board)
        it.start()

        while True:
            event = keyboard.read_event()
            for i, pin in enumerate(pins):
                if event.event_type == keyboard.KEY_DOWN and event.name == self.pins[i][6]:
                    # TODO: add functionality for positive key pressed
                    if self.pin[i][3] == 's': # Pin is 'Servo'
                        # TODO: add generic step size to current servo position
                        pass
                    elif self.pin[i][3] == 'o': # Pin is Output
                        # TODO: write a 1 to the output pin to turn on
                        pass
                    elif self.pin[i][3] == 'i': # Pin is 'Input'
                        pass
                    else: # Pin is 'PWM'
                        pass
                elif event.event_type == keyboard.KEY_DOWN and event.name == self.pins[i][7]:
                    # TODO: add functionality for negative key pressed
                    if self.pin[i][3] == 's': # Pin is 'Servo'
                        # TODO: subtract generic step size to current servo position
                        pass
                    elif self.pin[i][3] == 'o': # Pin is Output
                        # TODO: write a 0 to the output pin to turn off
                        pass
                    elif self.pin[i][3] == 'i': # Pin is 'Input'
                        pass
                    else: # Pin is 'PWM'
                        pass