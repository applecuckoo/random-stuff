# colormusic_fusion.py - colors and music fused together

from adafruit_circuitplayground import cp

# Setup - brightness and indicator
cp.pixels.brightness = 0.3
cp.red_led = True

# Middle C and Red
cp.pixels.fill((255, 0, 0))
cp.play_tone(262, 1)
print("Middle C and Red")

# Middle D and Blue
cp.pixels.fill((0, 0, 255))
cp.play_tone(294, 1)
print("Middle D and Blue")

# Middle E and Green
cp.pixels.fill((0, 255, 0))
cp.play_tone(330, 1)
print("Middle E and Green")

# Middle F and Yellow
cp.pixels.fill((255, 255, 0))
cp.play_tone(349, 1)
print("Middle F and Yellow")

# Middle G and Pink
cp.pixels.fill((249, 135, 197))
cp.play_tone(392, 1)
print("Middle G and Pink")

# Middle A and Purple
cp.pixels.fill((99, 0, 99))
cp.play_tone(440, 1)
print("Middle A and Purple")

# Middle B and Cyan
cp.pixels.fill((0, 255, 255))
cp.play_tone(494, 1)
print("Middle B and Cyan")

# High C and Brown
cp.pixels.fill((169, 120, 53))
cp.play_tone(523, 1)
print("High C and Brown")

# Turn off indicator
cp.red_led = False