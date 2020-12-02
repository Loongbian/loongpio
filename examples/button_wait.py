from loongpio import Button
from loongpio.pins import *

btn = Button(GPIO4)
btn.wait_until_press()
print('Button is pressed')
