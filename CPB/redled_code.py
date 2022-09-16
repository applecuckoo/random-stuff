from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led = not cp.red_led
    time.sleep(0.5)