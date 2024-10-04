"""
Created by: Gavin Gallant
Created on: Oct 2024
This module is a Micro:bit MicroPython program when we hit A all of the colors of an RGB light light up in sequence.
"""

from microbit import *

display.clear()
pin13.write_digital(0)
pin14.write_digital(0)
pin15.write_digital(0)
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        pin13.write_digital(1)
        display.scroll("Red")
        pin13.write_digital(0)

        pin15.write_digital(1)
        display.scroll("Blue")
        pin15.write_digital(0)

        pin14.write_digital(1)
        display.scroll("Green")
        pin14.write_digital(0)

        pin13.write_digital(1)
        pin15.write_digital(1)
        display.scroll("Magenta")
        pin13.write_digital(0)
        pin15.write_digital(0)

        pin14.write_digital(1)
        display.scroll("Cyan")
        pin14.write_digital(0)

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
