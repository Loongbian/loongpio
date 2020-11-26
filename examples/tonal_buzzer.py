from loongpio import TonalBuzzer
from loongpio.pins import *
from time import sleep

notes = ['C', 'D', 'E', 'F', 'G']
buzzer = TonalBuzzer(PWM0)

for note in notes:
    print('Playing ' + note)
    buzzer.play(note)
    sleep(1)
