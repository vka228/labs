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

def cls():
    while gpio.input(knop_in) == 0:
        print('door closesd')
        time.sleep(0.1)
    print('door opened')

volt = []
f = open("/home/b03-304/bebememe/data_120.txt", "w+")
try:
    while True:
        if gpio.input(knop_in) == 1:
            volt.append(adc()/256*3.3)
            print(volt)
            time.sleep(0.1)
            f.write(str(adc())+'\n')
            #f.write(str(adc()/256*3.3))

        



finally:
    f.close()
    #time = np.linspace(0, len(volt), len(volt)) * 0.1
    #plt.plot(time, volt)
    #plt.show() 
