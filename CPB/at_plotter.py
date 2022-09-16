# at_plotter.py - Acceleration and Temperature
import time
from adafruit_circuitplayground import cp

while True:
    # Sets xyz variable to individual axes
    x, y, z = cp.acceleration
    # Prints acceleration and temperature to serial
    print("Acceleration:", x, y, z)
    print("Temperature:", cp.temperature)
    # Prints combined value to serial for Mu Plotter
    print((x, y, z, cp.temperature))
    time.sleep(0.2)