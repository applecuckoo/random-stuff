# ls_plotter.py - light and sound plotter.
import time
from adafruit_circuitplayground import cp

# while true forever loop
while True:
    # Sound level
    print("Sound level:", cp.sound_level)
    # Light level
    print("Light level:", cp.light)
    # Combined value for Mu Plotter
    print((cp.sound_level, cp.light))
    # Break to prevent data floods
    time.sleep(0.2)