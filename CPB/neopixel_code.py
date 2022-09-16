from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    cp.pixels[0:2] = [(255, 0, 0)] * 2
    time.sleep(0.5)
    cp.pixels.fill((0, 0, 0))
    cp.pixels[8:10] = [(0, 0, 255)] * 2
    time.sleep(0.5)
    cp.pixels.fill((0, 0, 0))
    cp.pixels[5:7] = [(0, 255, 0)] * 2
    time.sleep(0.5)
    cp.pixels.fill((0, 0, 0))
    cp.pixels[3:5] = [(255, 255, 0)] * 2
    time.sleep(0.5)
    cp.pixels.fill((0, 0, 0))