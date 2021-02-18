from machine import Pin
import utime

relay1 = Pin(2, Pin.OUT)
relay2 = Pin(3, Pin.OUT)
relay3 = Pin(4, Pin.OUT)
relay4 = Pin(5, Pin.OUT)

while True:
    relay1.toggle()
    utime.sleep(0.5)
    relay2.toggle()
    utime.sleep(0.5)
    relay3.toggle()
    utime.sleep(0.5)
    relay4.toggle()
    utime.sleep(0.5)
    relay1(1)
    utime.sleep(0.5)
    relay1(0)
    utime.sleep(0.5)
