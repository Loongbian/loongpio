from loongpio import DistanceSensor
from loongpio.pins import *
from time import sleep

sensor = DistanceSensor(echo=GPIO3, trigger=GPIO4)

while True:
    print('Distance: %s cm' % sensor.distance)
    sleep(1)
