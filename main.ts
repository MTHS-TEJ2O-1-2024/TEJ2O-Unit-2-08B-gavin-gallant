/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Gavin Gallant
 * Created on: oct 2024
 * This program when we hit A, all of the colors of an RGB LED light up in sequence
*/

// Clear the display
basic.clearScreen()

// Set all pins to off
pins.digitalWritePin(DigitalPin.P13, 0)
pins.digitalWritePin(DigitalPin.P14, 0)
pins.digitalWritePin(DigitalPin.P15, 0)

// Show happy icon
basic.showIcon(IconNames.Happy)

// Handle button A press
input.onButtonPressed(Button.A, function () {
    // Red LED
    pins.digitalWritePin(DigitalPin.P13, 1)
    basic.showString("Red")
    pins.digitalWritePin(DigitalPin.P13, 0)

    // Blue LED
    pins.digitalWritePin(DigitalPin.P14, 1)
    basic.showString("blue")
    pins.digitalWritePin(DigitalPin.P14, 0)

    // Green LED
    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("Green")
    pins.digitalWritePin(DigitalPin.P15, 0)

    // Magenta (Red + Blue)
    pins.digitalWritePin(DigitalPin.P13, 1)
    pins.digitalWritePin(DigitalPin.P14, 1)
    basic.showString("magenta")
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.digitalWritePin(DigitalPin.P14, 0)

    // Cyan (Blue + Green)
    pins.digitalWritePin(DigitalPin.P14, 1)
    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("Cyan")
    pins.digitalWritePin(DigitalPin.P14, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)

    // Yellow (Red + Green)
    pins.digitalWritePin(DigitalPin.P13, 1)
    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("yellow")
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)

    // White (All LEDs on)
    pins.digitalWritePin(DigitalPin.P13, 1)
    pins.digitalWritePin(DigitalPin.P14, 1)
    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("white")

    // Turn off all LEDs
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.digitalWritePin(DigitalPin.P14, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)
})