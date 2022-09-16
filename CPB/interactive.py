from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led = cp.switch
    print("Light:", cp.light)
    print("Temp:", cp.temperature)
    """Green is temp, blue is light"""
    print((cp.light, cp.temperature))

    if cp.loud_sound(sound_threshold=600):
        cp.pixels.fill((0, 50, 0))
        time.sleep(0.5)
    elif cp.shake(shake_threshold=20):
        cp.pixels.fill((0, 50, 50))
        time.sleep(0.5)
    elif cp.button_a:
        cp.start_tone(262)
    elif cp.button_b:
        cp.start_tone(294)
    else:
        """Duplication of commands so tone doesn't get stuck"""
        cp.stop_tone()
        cp.stop_tone()
        cp.pixels.fill((0, 0, 0))