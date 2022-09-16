# animaltime_emulator.py - a trigger for cowsay and parrotsay
import usb_hid
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_gizmo import tft_gizmo
from adafruit_display_text import label
import terminalio
import displayio

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
display = tft_gizmo.TFT_Gizmo()
print("Please install Parrotsay, Cowsay and its dependencies on a *nix like OS before use.")

while True:
    if cp.button_a:
        # Type cowsay command followed by enter (a newline).
        layout.write('cowsay -f udder Moo!')
        print("Moo!")
        while cp.button_a:
            pass
    if cp.button_b:
        # Type parrotsay command followed by enter (a newline).
        layout.write('parrotsay Caw!')
        print("Caw!")
        while cp.button_b:
            pass