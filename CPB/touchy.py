import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
    if cp.touch_A1:
        print("Touched A1!")
        cp.pixels[6] = (255, 0, 0)
        cp.play_tone(262, 1)
    if cp.touch_A2:
        print("Touched A2!")
        cp.pixels[8] = (210, 45, 0)
        cp.play_tone(294, 1)
    if cp.touch_A3:
        print("Touched A3!")
        cp.pixels[9] = (155, 100, 0)
        cp.play_tone(330, 1)
    if cp.touch_A4:
        print("Touched A4!")
        cp.pixels[0] = (0, 255, 0)
        cp.play_tone(349, 1)
    if cp.touch_A5:
        print("Touched A5!")
        cp.pixels[1] = (0, 135, 125)
        cp.play_tone(392, 1)
    if cp.touch_A6:
        print("Touched A6!")
        cp.pixels[3] = (0, 0, 255)
        cp.play_tone(440, 1)
    if cp.touch_TX:
        print("Touched TX!")
        cp.pixels[4] = (100, 0, 155)
        cp.play_tone(494, 1)
    time.sleep(0.1)