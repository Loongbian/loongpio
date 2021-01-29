import loongpio
from loongpio.pins import *
from time import sleep

bh1750 = loongpio.BH1750(IIC0_SCL, IIC0_SDA)

while True:
    print('%.2f Lux' % bh1750.lux)
    sleep(1)
