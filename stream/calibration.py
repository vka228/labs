import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

###########################################################################
#Калибровочный график зависимости перемещения трубки Пито от шага двигателя
###########################################################################

x = [0, 500]
y = [0, 28] #в мм

np_x = np.array(x)
np_y = np.array(y)
fig, ax = plt.subplots()

ax.plot(np_x, np_y, label="Измерения",
        marker="*", linestyle="",
        linewidth=1)

ax.plot(np_x, np_y, label="X = {alfa} * step [мм]".format(alfa = round((y[1]-y[0]) / (x[1]-x[0]), 4)),
        marker="", linestyle="-",
        color='r', linewidth=1)

ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()

#plt.title("Калибровочный график\nзависимости перемещения трубки Пито от шага двигателя")
plt.xlabel("Колличество шагов", size=10)
plt.ylabel("Перемещение трубки Пито [см]", size=10)
plt.legend()
plt.show()
fig.savefig('Calibration-one.png', dpi=600)

###########################################################
#Калибровочный график зависимости показаний АЦП от давления
###########################################################

x = [0, 6.4] #в Паскалях
y = [963, 1415]

x1 = [0, 115]
y1 = [963, 1722]

np_x = np.array(x1)
np_y = np.array(y1)
fig, ax = plt.subplots()

ax.plot(np_x, np_y, label="Измерения",
        marker="*", linestyle="",
        linewidth=1)

ax.plot(np_x, np_y, label="P = {alfa} * N - 145.90 [Па]".format(alfa = round((x1[1]-x1[0]) / (y1[1]-y1[0]), 2)),
        marker="", linestyle="-",
        color='r', linewidth=1)

ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()

#plt.title("Калибровочный график\nзависимости показаний АЦП от давления")
plt.xlabel("Давление [Па]", size=10)
plt.ylabel("Отсчёты АЦП", size=10)
plt.legend()
plt.show()
fig.savefig('Calibration-two.png', dpi=600)