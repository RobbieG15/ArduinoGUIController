# imports
from tkinter import *
from tkinter import ttk
import dataCollectionStorage
import controller



# initializing gui
root = Tk()
root.geometry('500x500')
frm = ttk.Frame(root, padding = 10)
frm.grid()

# gui functions and variables needed

def destroyWidgets(widgets):
    for widget in widgets:
        widget.destroy()

def collectBoardAndPort(board, port):
    try:
        #controller.connect(board, port)
        destroyWidgets([boardDropDown, portDropDown, confirmBoardAndPort, boardText, portText])
        addPin()
    except:
        print('Port selection was wrong or board type was wrong. Change and resubmit.')

def displayPinFail():
    pass

def saveAndAdd(pinNum, pinType, pinMode):
    passed = controller.checkPin(pinNum, pinType, pinMode)
    if not passed:
        displayPinFail()
        addPin()
def saveAndQuit(pinNum, pinType, pinMode):
    passed = controller.checkPin(pinNum, pinType, pinMode)
    if not passed:
        displayPinFail()
        addPin()

# gui contents
# header
title = ttk.Label(frm, text = 'Arduino I/O Controller')
title.grid(row=0, column=0, columnspan=2)


# exit button
exitButton = ttk.Button(frm, text="Quit", command=root.destroy)
exitButton.grid(row=0, column=3)

# drop down board type
boards = ['Arduino', 'ArduinoMega']
boardType = StringVar(root)
boardType.set(boards[0])
boardText = ttk.Label(frm, text = 'Board Type:')
boardText.grid(row=1, column=0, columnspan=2)
boardDropDown = OptionMenu(frm, boardType, *boards)
boardDropDown.grid(row=1, column=3)

# drop down port selection
ports = dataCollectionStorage.getPorts()
portType = StringVar(root)
portType.set(ports[0])
portText = ttk.Label(frm, text = 'Port Type:')
portText.grid(row=2, column=0, columnspan=2)
portDropDown = OptionMenu(frm, portType, *ports)
portDropDown.grid(row=2, column=3)


# confirm board and port button
confirmBoardAndPort = Button(frm, text='Done', command=lambda: collectBoardAndPort(boardType.get(), portType.get()))
confirmBoardAndPort.grid(row=3, column=0, columnspan=4, sticky=E)

# adding pins

def addPin():
    col = 0
    row = 1
    pinNumText = ttk.Label(frm, text = 'Pin Number:')
    pinNumText.grid(column=col, row=row)
    pinNum = IntVar(root)
    pinNumDropDown = OptionMenu(frm, pinNum, *[item for item in range(1,21)])
    pinNumDropDown.grid(column=col+1, row=row)
    pinTypeText = ttk.Label(frm, text='Pin Type:')
    pinTypeText.grid(column=col, row=row+1)
    pinType = StringVar(root)
    pinTypeDropDown = OptionMenu(frm, pinType, *['Analog', 'Digital'])
    pinTypeDropDown.grid(column=col+1, row=row+1)
    pinModeText = ttk.Label(frm, text='Pin Mode:')
    pinModeText.grid(column=col, row=row+2)
    pinMode = StringVar(root)
    pinModeDropDown = OptionMenu(frm, pinMode, *['Input', 'Output', 'PWM', 'Servo'])
    pinModeDropDown.grid(column=col+1, row=row+2)
    addButton1 = ttk.Button(frm, text='Add and Continue', command=lambda: saveAndAdd(pinNum.get(), pinType.get(), pinMode.get()))
    addButton1.grid(column=col, row=row+3)
    addButton2 = ttk.Button(frm, text='Add and Quit', command=lambda: saveAndQuit(pinNum.get(), pinType.get(), pinMode.get()))
    addButton2.grid(column=col+1, row=row+3)


# running main gui loop
root.mainloop()