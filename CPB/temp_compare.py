import microcontroller
import time
from adafruit_circuitplayground import cp

while True:
    core_temp = microcontroller.cpu.temperature
    therm_temp = cp.temperature

    if core_temp > therm_temp:
        result1 = core_temp - therm_temp
        print("NRF:",core_temp, "Thermistor:",therm_temp)
        time.sleep(0.5)
        print("Difference:", result1)
    elif therm_temp > core_temp:
        result2 = therm_temp - core_temp
        print("Thermistor:",therm_temp, "NRF:",core_temp)
        time.sleep(0.5)
        print("Difference:", result2)
        time.sleep(0.5)
    else:
        print("Thermistor:",therm_temp, "NRF:",core_temp)
        time.sleep(0.5)