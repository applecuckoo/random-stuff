from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    # check if switch is on
    if cp.switch:
        # Switch off LED if still on from quiet mode - normal mode
        cp.red_led = False
        cp.pixels[0:2] = [(255, 0, 0)] * 2
        cp.play_tone(277, 0.25)
        # Blanking code
        cp.pixels.fill((0, 0, 0))
        cp.pixels[8:10] = [(0, 0, 255)] * 2
        cp.play_tone(370, 0.25)
        cp.pixels.fill((0, 0, 0))
        cp.pixels[5:7] = [(0, 128, 0)] * 2
        cp.play_tone(277, 0.25)
        cp.pixels.fill((0, 0, 0))
        cp.pixels[3:5] = [(255, 215, 0)] * 2
        cp.play_tone(415, 0.5)
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.5)
    else:
        # Quiet mode blinky
        cp.red_led = not cp.red_led
        time.sleep(0.5)