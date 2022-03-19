from serial.tools.list_ports import comports

def getPorts():
    portNames = []
    availablePorts = comports()
    for port in availablePorts:
        portNames.append(port[0])
    return portNames
