from adafruit_platformdetect import Detector
from adafruit_platformdetect.board import Board
from adafruit_platformdetect.chip import Chip

from adafruit_platformdetect.constants.chips import GS264E
from adafruit_platformdetect.constants.boards import LOONGSON_PI_2K_EDU

detector = Detector()

if detector.chip.id != GS264E or detector.board.id != LOONGSON_PI_2K_EDU:
    raise RuntimeError('Invalid platform. Loongpio is only supported on Loongson Pi 2K Edu platforms.')
else:
    from board import *
    PIN2 = IIC1_SDA
    PIN5 = IIC1_SCL
    PIN7 = GPIO7
    PIN11 = GPIO60
    PIN12 = GPIO1
    PIN13 = GPIO2
    PIN15 = GPIO3
    PIN16 = GPIO4
    PIN18 = GPIO5
    PIN22 = GPIO6
    PIN27 = IIC0_SDA
    PIN28 = IIC0_SCL
    PIN29 = GPIO8
    PIN31 = GPIO9
    PIN32 = GPIO10
    PIN33 = GPIO11
    PIN35 = GPIO12
    PIN36 = GPIO37
    PIN37 = GPIO13
    PIN38 = GPIO38
    PIN39 = GPIO40
    PIN40 = GPIO41
    PIN41 = GPIO56
    PIN42 = GPIO57
    PIN43 = GPIO58
    PIN44 = GPIO59
    PIN45 = PWM0
    PIN46 = PWM1
    PIN47 = PWM2
    PIN48 = PWM3


