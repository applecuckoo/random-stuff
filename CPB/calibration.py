# calibration.py
from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    # check if buttons are pressed
    if cp.button_a and cp.button_b == True:
        print("Testcard beep")
        cp.pixels.fill(0x0000FF)
        cp.play_tone(1000, 1)
        cp.pixels.fill(0x000000)
        print("A4, calibration tone")
        cp.pixels.fill(0xFF0000)
        cp.play_tone(440, 1)
        cp.pixels.fill(0x000000)