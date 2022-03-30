# imports
from audioop import add
from tkinter import *
from tkinter import ttk
import dataCollectionStorage



# initializing gui
root = Tk()
root.geometry('750x750')
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

def getServos(pinNum, pinType, pinMode, pinName, pinKeybind, lowDegree, highDegree):
    clearFrame()
    global addBool
    preset.pins.append((pinName, pinType, pinNum, pinMode, pinKeybind, lowDegree, highDegree))
    if addBool == True:
        header()
        addPin()
        addBool = False
    else:
        mainMenu()

def saveAndAdd(pinNum, pinType, pinMode, pinName, pinKeybind):
    clearFrame()
    global addBool
    addBool = True
    if pinMode == 's':
        header()
        setServos(pinNum, pinType, pinMode, pinName, pinKeybind)
    else:
        preset.pins.append((pinName, pinType, pinNum, pinMode, pinKeybind, 0, 1))
        header()
        addPin()

def saveAndQuit(pinNum, pinType, pinMode, pinName, pinKeybind):
    clearFrame()
    global addBool
    addBool = False
    if pinMode == 's':
        header()
        setServos(pinNum, pinType, pinMode, pinName, pinKeybind)
    else:
        preset.pins.append((pinName, pinType, pinNum, pinMode, pinKeybind, 0, 1))
        mainMenu()
    preset.save()

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
    pinKeybindText = ttk.Label(frm, text='Pin Keybind:')
    pinKeybindText.grid(column=col, row=row+4)
    pinKeybindInput = ttk.Entry(frm)
    pinKeybindInput.grid(column=col+1, row=row+4)
    addButton1 = ttk.Button(frm, text='Add and Continue', command=lambda: saveAndAdd(pinNum.get(), pinType.get(), pinMode.get(), pinName.get(), pinKeybindInput.get()))
    addButton1.grid(column=col, row=row+5)
    addButton2 = ttk.Button(frm, text='Add and Quit', command=lambda: saveAndQuit(pinNum.get(), pinType.get(), pinMode.get(), pinName.get(), pinKeybindInput.get()))
    addButton2.grid(column=col+1, row=row+5)
    
# servo settings
def setServos(pinNum, pinType, pinMode, pinName, pinKeybind):
    lowDegreeText = ttk.Label(frm, text="Low Degree")
    lowDegreeText.grid(column=0, row=1)
    lowDegreeInput = ttk.Entry(frm)
    lowDegreeInput.grid(column=1, row=1)
    highDegreeText = ttk.Label(frm, text="High Degree")
    highDegreeText.grid(column=0, row=2)
    highDegreeInput = ttk.Entry(frm)
    highDegreeInput.grid(column=1, row=2)
    doneButton = ttk.Button(frm, text='Done', command=lambda: getServos(pinNum, pinType, pinMode, pinName, pinKeybind, lowDegreeInput.get(), highDegreeInput.get()))
    doneButton.grid(column=1, row=3)

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