from machine import UART
import utime
import pycom

uart = UART(0, baudrate=115200, pins=('P0','P1'))

while True:
    for i in range(10):
        uart.write("This is a test: {}\n".format(i))
        print("Test")
        utime.sleep_ms(1000)
