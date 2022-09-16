# OutputSwitch.py - tests NeoPixels, red LED, buzzer, buttons and slide switch

from adafruit_circuitplayground import cp
import time

# Print variable
eightbit = False

# Frequencies
c = 262
e = 330
f = 349
g = 392
a = 440

# Brightness
cp.pixels.brightness = 0.25

# Set pixels to W3C values
# Red
cp.pixels[0] = (0xff0000)
# Dark orange, set for contrast
cp.pixels[1] = (0xff8c00)
# Yellow
cp.pixels[2] = (0xffff00)
# Lawn green
cp.pixels[3] = (0x7cfc00)
# Green
cp.pixels[4] = (0x008000)
# Cyan
cp.pixels[5] = (0x00ffff)
# Dark blue for contrast
cp.pixels[6] = (0x00008b)
# Indigo purple
cp.pixels[7] = (0x4b0082)
# Purple
cp.pixels[8] = (0x800080)
# Salmon
cp.pixels[9] = (0xfa8072)

while True:
    cp.red_led = not cp.red_led
    time.sleep(0.25)
    if cp.button_a and cp.button_b and cp.switch:
        cp.play_tone(c, 0.25)
        cp.play_tone(a, 0.25)
        cp.play_tone(a, 0.25)
        cp.play_tone(g, 0.25)
        cp.play_tone(f, 0.25)
        cp.play_tone(g, 0.25)
        cp.play_tone(e, 0.5)