from loongpio import Button
from loongpio.pins import *
from time import sleep

btn = Button(GPIO4)

while True:
    print("Button status: " + str(btn.is_pressed))
    sleep(0.5)
