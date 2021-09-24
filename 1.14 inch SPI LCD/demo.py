import random
from machine import Pin, SPI, ADC
import st7789
import utime

import vga1_bold_16x32 as font

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)



spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
LCD = st7789.ST7789(
    spi,
    135,
    240,
    reset=Pin(12, Pin.OUT),
    cs=Pin(9, Pin.OUT),
    dc=Pin(8, Pin.OUT),
    backlight=Pin(13, Pin.OUT),
    rotation=1)

LCD.init()
utime.sleep(0.5)

LCD.fill_rect(0, 00, 240,20, st7789.RED)
LCD.fill_rect(0, 90, 240,20, st7789.YELLOW)
LCD.fill_rect(0, 110, 240,20, st7789.CYAN)


while True:
    
    reading = sensor_temp.read_u16() * conversion_factor
    
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    
    LCD.text(font, "TEMP:{:.2f}".format(temperature), 40,40)
    print("TEMPERATURE:{:.2f}".format(temperature))
    utime.sleep(1)
