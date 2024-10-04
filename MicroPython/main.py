"""
Created by: Gavin Gallant
Created on: oct 2024
This module is a Micro:bit MicroPython program when we hit A all of the coulors of a RGB light light up in sequence
"""

from microbit import *

display.clear()
pin13.write_digital(0)
pin14.write_digital(0)
pin15.write_digital(0)
display.show(Image.HAPPY)

def show_color(pin, color_name):
    pin.write_digital(1)
    display.scroll(color_name)
    pin.write_digital(0)

while True:
    if button_a.is_pressed():
        show_color(pin13, "Red")
        show_color(pin14, "Blue")
        show_color(pin15, "Green")
        
        pin13.write_digital(1)
        pin14.write_digital(1)
        display.scroll("Magenta")
        
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Cyan")
        
        pin14.write_digital(0)
        pin15.write_digital(0)
        pin13.write_digital(1)
        pin15.write_digital(1)
        display.scroll("Yellow")
        
        pin13.write_digital(0)
        pin15.write_digital(0)
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(1)
        display.scroll("White")
        
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
