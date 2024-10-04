"""
Created by: Gavin Gallant
Created on: Oct 2024
This module is a Micro:bit MicroPython program that lights up all colors of an RGB light in sequence when button A is pressed.
"""

from microbit import *

# Initialize the display and pins
display.clear()
pin13.write_digital(0)  # Red pin
pin14.write_digital(0)  # Green pin
pin15.write_digital(0)  # Blue pin
display.show(Image.HAPPY)  # Show a happy face

while True:
    if button_a.is_pressed():
        # Light up Red
        pin13.write_digital(1)
        display.scroll("Red")
        pin13.write_digital(0)

        # Light up Blue
        pin15.write_digital(1)
        display.scroll("Blue")
        pin15.write_digital(0)

        # Light up Green
        pin14.write_digital(1)
        display.scroll("Green")
        pin14.write_digital(0)

        # Light up Magenta
        pin13.write_digital(1)
        pin15.write_digital(1)
        display.scroll("Magenta")
        pin13.write_digital(0)
        pin15.write_digital(0)

        # Light up Cyan
        pin14.write_digital(1)
        display.scroll("Cyan")
        pin14.write_digital(0)

        # Light up Yellow
        pin13.write_digital(1)
        pin14.write_digital(1)
        display.scroll("Yellow")
        pin13.write_digital(0)
        pin14.write_digital(0)

        # Light up White
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(1)
        display.scroll("Yellow")
        # turn all pins off
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)