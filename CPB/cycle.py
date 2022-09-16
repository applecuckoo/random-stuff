from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    # check if switch is on
    if cp.switch:
        # Switch off LED if still on from quiet mode - normal mode
        cp.red_led = False
        # Red and Middle C with built in timing
        cp.pixels[0:2] = [(255, 0, 0)] * 2
        cp.play_tone(262, 0.5)
        # Blanking code
        cp.pixels.fill((0, 0, 0))
        # Blue and E
        cp.pixels[8:10] = [(0, 0, 255)] * 2
        cp.play_tone(330, 0.5)
        cp.pixels.fill((0, 0, 0))
        # Green and G
        cp.pixels[5:7] = [(0, 255, 0)] * 2
        cp.play_tone(392, 0.5)
        cp.pixels.fill((0, 0, 0))
        # Yellow and High C
        cp.pixels[3:5] = [(255, 255, 0)] * 2
        cp.play_tone(523, 0.5)
        cp.pixels.fill((0, 0, 0))
    else:
        # Quiet mode blinky
        cp.red_led = not cp.red_led
        time.sleep(0.5)
