from machine import Pin
import utime

relay1 = Pin(18, Pin.OUT)
relay2 = Pin(19, Pin.OUT)
relay3 = Pin(20, Pin.OUT)
relay4 = Pin(21, Pin.OUT)

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
