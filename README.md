# ArduinoGUIController

## Usage

This app was made for operating Arduino boards in an easier way than using the `Arduino IDE` or even writing any code at all. The purpose of this program will be to have a graphical user interface that lets you connect Arduino style boards to a computer, establish pin connections for either `Input`, `Output`, `Servo`, or `PWM`, and operate these pins via the keyboard. So far, this application has been tested using a robotic arm with various `servos` connected to it.

## Features

This app features compatibility with `Arduino Mega`, `Arduino Nano`, `Arduino Due`, and `Arduino`. The program dynamically finds ports based on your system and will allow you to try to connect to them via `usb` or `bluetooth`. Not only can you connect to the `I/O` pins, you can also operate them using keybinds you set on the keyboard.

## Setup

### Arduino IDE and Setup

This repo has multiple ways to run `Servos` from a keyboard. It is meant to be compatible with an `Arduino Board` and the `firmata` library. In order to successfully use any of the controllers in this repo, you first need to install the `Arduino IDE`. From there you have to locate how to install the `firmata package` and orient the correct `port` within that `IDE` that your `Arduino` is attached to. The last thing you need to do is load the `StandardFirmata` code inside the `Arduino IDE` and run it. Once that is all set and completed without error, it is time to dive into the `Python` side of things.

### Python Setup

In terms of setup for `Python`, I recommend using a steady build of `Python3` because that is what I used to develop and test. Next, you need to download `requirements.txt` via pip. Use the command `pip install -r requirements.txt` in the terminal to do so. If that throws any type of error, try `pip3 install -r requirements.txt`. Otherwise, look up online to see how to use `pip` or install `pip` on your specific machine.

## Known Limitations

## Overall

The limitations with this program mostly come from not doing enough input checking on the user. I have not made much when it comes to taking input the person selects on the gui, and verifying it will work. Instead, I am going to try to connect to the preset they select and then offer the selection to update the preset settings if their was a failure at some point.

### Servo Output

The servo ouput has been tested the most and I can say there is a couple flaws. I need to add a `step size` when creating the pins via the gui. This is because someone might want to move their `servo` faster than the default `step size` I have set of 1 degree per keyboard press. Depending on the speed of the computer, this may fluctaute as well which I should take account for with some type of `delta time` implementation.

### On/Off Output

The on off input is still under development. When finished, it will allow you to just press a certain button to turn it on and a button to turn it off. The logic has been implemented, but I need to go back and test before I state any final results.

### Input 

The input is not yet implemented passed the connection of the pins. The pins will actually say they have been connected, but I have not yet decided how I want the input to be recorded and displayed back to the user. My idea is that when a button is pressed, it will display that most recently read value from that pin to the user.
