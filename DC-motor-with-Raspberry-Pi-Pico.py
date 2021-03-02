from machine import Pin
import utime

m1 = Pin(5, Pin.OUT)
m2 = Pin(4, Pin.OUT)
m3 = Pin(3, Pin.OUT)
m4 = Pin(2, Pin.OUT)

en1 = Pin(6, Pin.OUT)
en2 = Pin(7, Pin.OUT)

en1(1)  # motor 1 enable, set value 0 to disable
en2(1)  # motor 2 enable, set value 0 to disable

while True:
    #Both Motor in forward direction
    m1(1)
    m2(0)
    m3(1)
    m4(0)
    utime.sleep(1)
    #Both Motor in stop position
    m1(0)
    m2(0)
    m3(0)
    m4(0)
    utime.sleep(1)
    #Both Motor in Reverse direction
    m1(0)
    m2(1)
    m3(0)
    m4(1)
    utime.sleep(1)
