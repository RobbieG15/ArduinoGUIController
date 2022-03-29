# imports
from tkinter import *
from tkinter import ttk
from turtle import clear
import dataCollectionStorage
import controller



# initializing gui
root = Tk()
root.geometry('500x500')
frm = ttk.Frame(root, padding = 10)
frm.grid()

# gui functions and variables needed
def clearFrame():
   for widgets in frm.winfo_children():
      widgets.destroy()

def collectBoardAndPort(board, port, presetName):
    preset.presetName = presetName
    preset.board = board
    preset.port = port
    clearFrame()
    header()
    addPin()

def saveAndAdd(pinNum, pinType, pinMode, pinName):
    preset.pins.append((pinName, pinType, pinNum, pinMode))
    clearFrame()
    header()
    addPin()

def saveAndQuit(pinNum, pinType, pinMode, pinName):
    preset.pins.append((pinName, pinType, pinNum, pinMode))
    preset.save()
    clearFrame()
    mainMenu()

def showSavedList():
    presetNamesList = dataCollectionStorage.getPresetNames()
    clearFrame()
    header()
    selectSaved(presetNamesList)

def getPresetToRun(preset):
    pass



# gui contents
def selectNameBoardPort():
    # get rid of main menu options
    clearFrame()
    header()
    # new preset from data collection
    global preset 
    preset = dataCollectionStorage.Presets()
    # preset name
    presetNameText = ttk.Label(frm, text = 'Preset Name:')
    presetNameText.grid(row=1, column=0, columnspan=2)
    presetName = ttk.Entry(frm)
    presetName.grid(row=1, column=3)
    # drop down board type
    boards = ['Arduino', 'ArduinoMega']
    boardType = StringVar(root)
    boardType.set(boards[0])
    boardText = ttk.Label(frm, text = 'Board Type:')
    boardText.grid(row=2, column=0, columnspan=2)
    boardDropDown = OptionMenu(frm, boardType, *boards)
    boardDropDown.grid(row=2, column=3)

    # drop down port selection
    ports = dataCollectionStorage.getPorts()
    portType = StringVar(root)
    portType.set(ports[0])
    portText = ttk.Label(frm, text = 'Port Type:')
    portText.grid(row=3, column=0, columnspan=2)
    portDropDown = OptionMenu(frm, portType, *ports)
    portDropDown.grid(row=3, column=3)


    # confirm board and port button
    confirmBoardAndPort = Button(frm, text='Done', command=lambda: collectBoardAndPort(boardType.get(), portType.get(), presetName.get()))
    confirmBoardAndPort.grid(row=4, column=0, columnspan=4, sticky=E)

# adding pins
def addPin():
    col = 0
    row = 1
    pinNameText = ttk.Label(frm, text = 'Pin Name:')
    pinNameText.grid(column=col, row=row)
    pinName = ttk.Entry(frm)
    pinName.grid(column=col+1, row=row)
    pinNumText = ttk.Label(frm, text = 'Pin Number:')
    pinNumText.grid(column=col, row=row+1)
    pinNum = IntVar(root)
    pinNumDropDown = OptionMenu(frm, pinNum, *[item for item in range(1,21)])
    pinNumDropDown.grid(column=col+1, row=row+1)
    pinTypeText = ttk.Label(frm, text='Pin Type (Analog or Digital):')
    pinTypeText.grid(column=col, row=row+2)
    pinType = StringVar(root)
    pinTypeDropDown = OptionMenu(frm, pinType, *['a', 'd'])
    pinTypeDropDown.grid(column=col+1, row=row+2)
    pinModeText = ttk.Label(frm, text='Pin Mode (Input, Output, PWM, Servo):')
    pinModeText.grid(column=col, row=row+3)
    pinMode = StringVar(root)
    pinModeDropDown = OptionMenu(frm, pinMode, *['i', 'o', 'p', 's'])
    pinModeDropDown.grid(column=col+1, row=row+3)
    addButton1 = ttk.Button(frm, text='Add and Continue', command=lambda: saveAndAdd(pinNum.get(), pinType.get(), pinMode.get(), pinName.get()))
    addButton1.grid(column=col, row=row+4)
    addButton2 = ttk.Button(frm, text='Add and Quit', command=lambda: saveAndQuit(pinNum.get(), pinType.get(), pinMode.get(), pinName.get()))
    addButton2.grid(column=col+1, row=row+4)

# universal header
def header():
    # header
    title = ttk.Label(frm, text = 'Arduino I/O Controller')
    title.grid(row=0, column=0, columnspan=2, sticky=W)
    # exit button
    exitButton = ttk.Button(frm, text="Quit", command=root.destroy)
    exitButton.grid(row=0, column=3, sticky=E)

# main menu screen
def mainMenu():
    header()
    # new preset button
    newPresetButton = ttk.Button(frm, text="New Preset", command=selectNameBoardPort)
    newPresetButton.grid(row=1, column=0)
    # view saved presets
    viewSavedButton = ttk.Button(frm, text="Saved Presets", command=showSavedList)
    viewSavedButton.grid(row=1, column=1)

# select from saved presets
def selectSaved(presetNameList):
    # preset text
    selectPresetText = ttk.Label(frm, text="Select Preset:")
    selectPresetText.grid(row=1,column=0)
    # preset drop down
    preset = StringVar(root)
    presetDropDown = OptionMenu(frm, preset, *presetNameList)
    presetDropDown.grid(row=1, column=1)
    #confirm
    confirmPresetButton = ttk.Button(frm, text="Confirm", command=lambda: getPresetToRun(preset.get()))
    confirmPresetButton.grid(row=1, column=2, sticky=E)



# running main gui loop
mainMenu()
root.mainloop()