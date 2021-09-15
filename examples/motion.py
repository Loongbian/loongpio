from loongpio import MotionSensor
from loongpio.pins import *

motion_sensor = MotionSensor(GPIO4)
motion_sensor.wait_for_motion()
print('Motion is detected')
