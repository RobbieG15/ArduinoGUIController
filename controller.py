from pyfirmata import *

board = ''
pins = []

def connect(boardType, port):
    global board
    if boardType == 'Arduino':
        board = Arduino(port)

def checkPin(pinNum, pinType, pinMode):
    global board
    global pins
    try:
        if pinType == 'Digital':
            if pinMode == 'Servo':
                pin = board.get_pin('d:' + pinNum + ':o')
                pin.mode = SERVO
            elif pinMode == 'PWM':
                pin = board.get_pin('d:' + pinNum + ':p')
                pin.mode = PWM
            elif pinMode == 'Output':
                pin = board.get_pin('d:' + pinNum + ':o')
                pin.mode = OUTPUT
            else:
                pin = board.get_pin('d:' + pinNum + ':i')
                pin.mode = INPUT
        else:
            if pinMode == 'Servo':
                pin = board.get_pin('a:' + pinNum + ':o')
                pin.mode = SERVO
            elif pinMode == 'PWM':
                pin = board.get_pin('a:' + pinNum + ':p')
                pin.mode = PWM
            elif pinMode == 'Output':
                pin = board.get_pin('a:' + pinNum + ':o')
                pin.mode = OUTPUT
            else:
                pin = board.get_pin('a:' + pinNum + ':i')
                pin.mode = INPUT
        pins.append(pin)
        return True
    except InvalidPinDefError:
        print('The information entered does not match a pin. Try Again.')
        return False
    except PinAlreadyTakenError:
        print("Pin was already used. Select a different pin.")
        return False