from loongpio import Servo
from loongpio.pins import *
from time import sleep

servo = Servo(PWM0)

while True:
    servo.min()
    sleep(2)
    servo.mid()
    sleep(2)
    servo.max()
    sleep(2)
