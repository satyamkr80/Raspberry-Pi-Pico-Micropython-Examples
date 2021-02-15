from machine import Pin
import utime

button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    b1 = button.value()
    if not b1:
        print('Button pressed!')
        utime.sleep(0.5)
