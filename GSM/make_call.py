from machine import Pin
import utime
import uos


uart0 = machine.UART(0,baudrate=9600)   #at-comand

#2 sec timeout is arbitrarily chosen
def sendCMD_waitResp(cmd, uart=uart0, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd)
    waitResp(uart, timeout)
    print()
    
def waitResp(uart=uart0, timeout=2000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read()])
            
            if resp != '':
                print(resp.decode())   

   
sendCMD_waitResp("AT+CGATT?\r\n")
utime.sleep(2)
sendCMD_waitResp("ATDxxxxxxxxxx;\r\n")  #Replace xxxxxxxx with monile number
utime.sleep(8)
sendCMD_waitResp("ATH\r\n")   # Hang call
