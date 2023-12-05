import jetFunctions as jet
import time

import RPi.GPIO as GPIO
import spidev
import matplotlib.pyplot as plt

########################################
# Setting up SPI device
# and read function for MCU
########################################

########################################
# Setting up GPIO pins for MCU control
########################################


steps = 1000
k = 6.6
kR = 0.0056 
p0 = 963
f = True

measures = []
R = []
VR = []
V = []

try:
    jet.initSpiAdc()
    jet.initStepMotorGpio()

    # iter = 6
    # p0 = 0
    # for i in range (iter):
    #     p0 = p0 + jet.getAdc()
    #     time.sleep(0.5)
    # p0 = p0/iter
    # print (str(p0) + "\n Now we are ready to start!" + "\n Press 0 to start show:")

    # while (f):
    #     if (int(input()) == 0):
    #         f = False
    

    
    

    for i in range (steps ):
        jet.stepBackward(1)
        measures.append((jet.getAdc() - p0) / k)
        R.append(i * kR)
        time.sleep(0.1)
    jet.stepForward(steps)
    

    for i in range (steps):
        print (measures[i])

    with open("/home/b03-303/Desktop/lab_work/v_70.txt", 'w') as f:
        for i in range(steps):
            speed = (2 * measures[i] / 1.2) ** 0.5 - 6
            V.append(speed)
            VR.append(speed * R[i])
            f.write(str(speed))
            f.write('\n') 
    
    with open("/home/b03-303/Desktop/lab_work/r_70.txt", 'w') as fil:
        for i in range(steps):
            fil.write(str(R[i]))
            fil.write('\n') 

    plt.scatter(R, V)
    plt.show()
    for i in range(steps):
        if R[i] > 0.7:
            VR[i] = 0
    plt.scatter(R, VR, color = 'r')
    plt.show()

    #разовое измерение для отладки(поиска tg) 
    # iter = 6
    # s = 0
    # for i in range (iter):
    #     m = jet.getAdc()
    #     s = s + m
    #     print (m)
    #     time.sleep(0.5)
    # print (s/iter)
    ########################################

finally:
    jet.deinitSpiAdc()
    jet.deinitStepMotorGpio()