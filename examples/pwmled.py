from loongpio import PWMLED
from loongpio.pins import *

from time import sleep

led = PWMLED(PWM0)

while True:
    led.value = 0 # 关闭
    sleep(1)
    led.value = 0.5 # 半亮
    sleep(1)
    led.value = 1 # 全亮
    sleep(1)
