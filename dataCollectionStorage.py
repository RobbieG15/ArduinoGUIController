from serial.tools.list_ports import comports

boardTypes = ['Arduino', 'ArduinoMega', 'ArduinoDue', 'ArduinoNano']

def getPorts():
    portNames = []
    availablePorts = comports()
    for port in availablePorts:
        portNames.append(port[0])
    return portNames

def getPresetNames():
    with open('presets.txt') as presets:
        presetNameList = []
        lines = presets.read().splitlines()
        for i in lines:
            if lines.index(i) % 4 == 0:
                presetNameList.append(i)
        return presetNameList


class Presets:
    def __init__(self):
        self.presetName = ''
        self.board = ''
        self.port = ''
        self.pins = [] # pins take form [name, d/a, num, (i/o/p/s)]

    def to_string(self):
        print(f'Preset: {self.presetName}\n')
        print(f'Board: {self.board}\n')
        print(f'Port: {self.port}\n')
        for pin in self.pins:
            print(f'{pin[0]} pin has settings as follows: type of {pin[1]}, pin num of {pin[2]}, and is in {pin[3]} mode.\n')

    def save(self):
        with open('presets.txt', 'a') as presets:
            presets.write(f'{self.presetName}\n')
            presets.write(f'{self.board}\n')
            presets.write(f'{self.port}\n')
            presets.write('[')
            for pin in self.pins:
                if self.pins.index(pin) == (len(self.pins) - 1):
                    presets.write(f'{pin}')
                else:
                    presets.write(f'{pin},  ')
            presets.write(']\n')
