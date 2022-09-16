# microplayground.py
from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    # check if switch is on
    if cp.switch == True:
        cp.pixels.fill((50, 50, 50))
        cp.play_tone(262, 0.5)
        cp.play_tone(329, 0.5)
        cp.play_tone(392, 0.5)
        cp.play_tone(523, 0.5)
        cp.pixels.fill(0x000000)
        cp.play_tone(523, 0.5)
        cp.play_tone(392, 0.5)
        cp.play_tone(329, 0.5)
        cp.play_tone(262, 0.5)