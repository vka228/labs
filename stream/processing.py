import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from math import pi

def integral(array_x, array_y):
  summa = 0
  for i in range(5, len(array_x)-6, 5):
    if 'j' in str(array_y[i]): array_y[i] = 0
    if 'j' in str(array_y[i+5]): array_y[i+5] = 0
    s = (array_y[i] + array_y[i+5]) * (array_x[i+5] - array_x[i]) / 2
    summa += s
  return summa

########################################

def grafics_speed(array_x, array_y, ax, p, q):
    max_el = 0
    for i in range(len(array_y[:400])-1):
        if ('j' in str(array_y[i])): array_y[i] = 0
        if (float(max_el) < float(array_y[i]) ): max_el = array_y[i]
    max_ind = array_y.index(max_el)
    flag = False
    for i in range(max_ind, -1, -1):
       if ('j' in str(array_y[i])): array_y[i] = 0
       if ('j' in str(array_y[i+1])): array_y[i+1] = 0
       if (array_y[i] * array_y[i-1] < 0 and not flag): flag = True
       if (flag): array_y[i] = 0
    flag = False
    for i in range(max_ind, len(array_x)-1):
        if ('j' in str(array_y[i])): array_y[i] = 0
        if ('j' in str(array_y[i+1])): array_y[i+1] = 0
        if (array_y[i] * array_y[i+1] < 0 and not flag): flag = True
        if (flag): array_y[i] = 0

    #ax.plot(array_x[150:420], array_y[150:420], label = "V ({p0} мм) = {v0} [м/с]; Q ({p0} мм) = {q0} [г/с]".format(p0 = p, v0 = round(max(array_y), 2), q0 = round(q, 3)),
    #        marker="", linestyle="-",
    #        linewidth=1)
    
    #ax.grid(which = "major", linewidth = 1)
    #ax.grid(which = "minor", linewidth = 0.2)
    #ax.minorticks_on()

def grafics_flow(array_x, array_y, ax, p):
    ind_null = array_x.index(0)
    array_x = array_x[ind_null:400]
    array_y = array_y[ind_null:400]

    max_el = 0
    for i in range(1, len(array_y)-1):
        if (array_y[i] < 0): break
        if ('j' in str(array_y[i])): array_y[i] = 0
        if (max_el < array_y[i] ): max_el = array_y[i]
    max_ind = array_y.index(max_el)
    flag = False

    for i in range(max_ind, len(array_x)-1):
        if (array_y[i] * array_y[i+1] < 0 and not flag): flag = True
        if (flag): array_y[i] = 0

    ax.plot(array_x[:130], array_y[:130], label = "{p0} мм".format(p0 = p),
            marker="", linestyle="-",
            linewidth=1)
    
    ax.grid(which = "major", linewidth = 1)
    ax.grid(which = "minor", linewidth = 0.2)
    ax.minorticks_on()

    return (2*pi*integral(array_x, array_y)*1.2*10**(-6))

########################################

def processing(array):
    for i in range(len(array)):
        array[i] = 0.15 * array[i] - 145.9
    return array

def arrays(p, ax):
    array_adc = []
    #распаковываем файл с данными ацп
    with open ("{p0}.txt".format(p0 = p)) as file:
        for f in file:
            array_adc.append(float(f.split()[0]))
    #конвертируем в паскали
    array_p = processing(array_adc)
    #зная давление, найдём скорость по формуле бернулли
    array_speed = [0] * 500
    for i in range(len(array_speed)):
        array_speed[i] = ( 2 * array_p[i] / ro ) ** 0.5 - 6
    #генерируем массив шагов
    array_step = [0] * 500
    max_el = 0
    for i in range(len(array_speed[:400])-1):
        if ('j' in str(array_speed[i])): array_speed[i] = 0
        if (max_el < array_speed[i] ): max_el = array_speed[i]
    max_ind = array_speed.index(max_el)
    for i in range(max_ind+1, 500):
        array_step[i] = array_step[i-1] + 1
    for i in range(max_ind-1, -1, -1):
        array_step[i] = array_step[i+1] - 1

    #конвертируем шаги в мм
    for i in range(len(array_step)):
        array_step[i] = 0.056 * array_step[i]
    #для определения потока потребуется массив v * r
    #v - скорость, r - шаг
    array_vr = [(array_speed[i] * 1000 * array_step[i]) for i in range(500)]
    q = grafics_flow(array_step, array_vr, ax, p)
    grafics_speed(array_step, array_speed, ax, p, q)

#const
ro = 1.2 #кг/м3
fig, ax = plt.subplots()
for i in range(0, 81, 10):
   arrays(str(i), ax)
#plt.title("Скорость потока воздуха\nв сечении затопленной струи")
#plt.xlabel("Положение трубки Пито относительно центра струи [мм]", size=10)
#plt.ylabel("Скорость воздуха [м/с]", size=10)
plt.xlabel("Положение трубки Пито r [мм]", size=10)
plt.ylabel("V(r)$\cdot$r [мм^2/с]", size=10)
plt.legend()
plt.show()
#fig.savefig('VelocityOutGo.png', dpi=1200)
fig.savefig('Flow.png', dpi=1200)