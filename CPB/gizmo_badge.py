"""Custom badge example for Adafruit CLUE."""
from adafruit_pybadger import pybadger


pybadger.badge_background(
    background_color=pybadger.WHITE,
    rectangle_color=pybadger.YELLOW,
    rectangle_drop=0.2,
    rectangle_height=0.6,
)

pybadger.badge_line(
    text="@aidancuckoo", color=pybadger.PYTHON_YELLOW, scale=2, padding_above=2
)
pybadger.badge_line(text="Aidan", color=pybadger.WHITE, scale=5, padding_above=3)
pybadger.badge_line(
    text="CircuitPythonista", color=pybadger.WHITE, scale=2, padding_above=2
)
pybadger.badge_line(
    text="he/his", color=pybadger.PYTHON_BLUE, scale=4, padding_above=4
)

pybadger.show_custom_badge()

while True:
    if pybadger.button.a:
        pybadger.show_qr_code("https://adafruit.com")

    if pybadger.button.b:
        pybadger.show_custom_badge()