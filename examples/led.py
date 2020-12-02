from loongpio import LED
from loongpio.pins import *
from time import sleep

led = LED(GPIO4)

while True:
    led.on()
    print('LED is on')
    sleep(1)
    led.off()
    print('LED is off')
    sleep(1)
