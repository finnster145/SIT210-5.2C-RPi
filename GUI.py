from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led = LED(14)
red = LED(18)


win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Halvetica', size = 12, weight = "bold")

def ledToggle():
	if led.is_lit:
		led.off()
		ledButton["text"] = "Turn Green LED on"
	else:
		led.on()
		ledButton["text"] = "Turn Green LED off"

def redToggle():
	if red.is_lit:
		red.off()
		redButton["text"] = "Turn Yellow LED on"
	else:
		red.on()
		redButton["text"] = "turn Yellow LED off"

def close():
	RPi.GPIO.cleanup()
	win.destroy()

ledButton = Button(win, text = 'Turn LED On', font = myFont, command = ledToggle, bg = 'green', height = 1, width = 24)
redButton = Button(win, text = 'Turn LED On', font = myFont, command = redToggle, bg = 'yellow', height = 1, width =24)
redButton.grid(row=1,column=1)
ledButton.grid(row=0,column=1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=2,column=1)

win.protocol("WM_DELETE_WINDOW", close)
