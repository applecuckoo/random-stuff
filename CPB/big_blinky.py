from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = (0.3)

while True:
    cp.red_led = True
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.5)
    cp.red_led = False
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.5)