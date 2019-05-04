from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
redled = LED(14)
blueled = LED(15)
greenled = LED(17)


## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = "Helvetica",size = 12, weight = "bold")

### EVENT FUNCTIONS ###

def blueToggle():
    if blueled.is_lit:
        blueled.off()
        blueButton["text"] = "Turn LED on"
    else:
        blueled.on()
        blueButton["text"] = "Turn LED off"
        
def redToggle():
    if redled.is_lit:
        redled.off()
        redButton["text"] = "Turn LED on"
    else:
        redled.on()
        redButton["text"] = "Turn LED off"

def greenToggle():
    if greenled.is_lit:
        greenled.off()
        greenButton["text"] = "Turn LED on"
    else:
        greenled.on()
        greenButton["text"] = "Turn LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
redButton = Button(win, text = "Turn LED on", font = myFont, command = redToggle, bg = "red", height = 1, width = 24)
redButton.grid(row=0, column=1)

blueButton = Button(win, text = "Turn LED on", font = myFont, command = blueToggle, bg = "blue", height = 1, width = 24)
blueButton.grid(row=1, column=1)

greenButton = Button(win, text = "Turn LED on", font = myFont, command = greenToggle, bg = "green", height = 1, width = 24)
greenButton.grid(row=2, column=1)

ExitButton = Button(win, text = "Exit", font = myFont, command = close, bg = "bisque2", height = 1, width = 6)
ExitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

win.mainloop() #loop forever


