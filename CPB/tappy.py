"""tappy.py - a demonstration of AI that lights up the NeoPixels
to cyan when double tapped."""
import time
from adafruit_circuitplayground import cp

# Change to 1 for detecting a single-tap!
cp.detect_taps = 2
cp.pixels.brightness = 0.3

while True:
    if cp.tapped:
        print("Tapped!")
        cp.pixels.fill((0, 255, 255))
        time.sleep(1)
    else:
        cp.pixels.fill((0, 0, 0))
