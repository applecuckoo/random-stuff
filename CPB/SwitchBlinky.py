# SwitchBlinky.py

from adafruit_circuitplayground import cp
import time

neoblink = False
indiblink = False

cp.pixels.brightness = 0.1

while True:
    if cp.switch:
        if neoblink is False:
            neoblink = True
            indiblink = False
            cp.red_led = False
        else:
            cp.pixels.fill((255, 0, 0))
            time.sleep(0.5)
            cp.pixels.fill((0, 0, 0,))
            time.sleep(0.5)
    else:
        if indiblink is False:
            indiblink = True
            neoblink = False
            cp.pixels.fill((0, 0, 0))
        else:
            cp.red_led = True
            time.sleep(0.5)
            cp.red_led = False
            time.sleep(0.5)
