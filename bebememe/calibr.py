import RPi.GPIO as gpio
from time import sleep
import time
import numpy as np
from matplotlib import pyplot as plt
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp=14

troyka = 13
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
knop_in=21

gpio.setup(knop_in, gpio.IN)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)

def binary(a):
    return [int (m) for m in bin(a)[2:].zfill(8)]
def adc():
    f = 0
    for i in range (7, -1, -1):
        f += 2**i
        gpio.output(dac, binary(f))
        time.sleep(0.001)
        if gpio.input(comp) == 1:
            f -= 2**i
    return f

f = open("/home/b03-304/bebememe/calibr_120.txt", "w+")


for i in range (100):

    f.write(str(adc())+'\n')
    time.sleep(0.1)
