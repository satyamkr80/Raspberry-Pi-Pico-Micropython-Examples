from machine import Pin, UART
import utime

led = Pin(25, Pin.OUT)
led(0)
uart = UART(1, baudrate=9600,
                    bits=8, parity=None, stop=1)

print(uart)

while True:
    #uart.write('h')
    command= uart.read(1)
    command= command.decode("utf-8")
    print(command)
    if command=='a':  #Turn Led on
        led(1)
    elif command=='b':   #Turn Led off
        led(0)
    


