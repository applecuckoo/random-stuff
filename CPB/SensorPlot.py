# SensorPlot.py - a sensor plot of all sensors on the Circuit Playground Bluefruit

from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch:
        x, y, z = cp.acceleration
        print((x, y, z, cp.sound_level))
        time.sleep(0.5)
    else:
        print((cp.light, cp.temperature))
        time.sleep(0.5)