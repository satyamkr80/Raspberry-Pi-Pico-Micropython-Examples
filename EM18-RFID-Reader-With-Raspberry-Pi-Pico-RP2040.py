from machine import Pin, UART
import utime


uart = UART(0, baudrate=9600,
                    bits=8, parity=None, stop=1)
print("EM18 With PICO By satyam Singh")
print("Tap Card Now")

while True:
    
    Card_ID= uart.read(12)
    Card_ID = Card_ID.decode("utf-8")
    if Card_ID:
        print(Card_ID)
        utime.sleep(0.5)
        Card_ID=""
