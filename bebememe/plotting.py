import matplotlib.pyplot as plt
import numpy as np
from main import d40, d80, d120, t40, t80, t120
from main import voltage, dp
from main import x_calibr
from main import wvtm40, wvtm80, wvtm120
from main import sp40, sp80, sp120, h_tst, sp_tst


# калибровочный график
# расстояне от двери до датчика - 143 см
fig1, ax1 = plt.subplots()
plt.scatter(voltage, dp)
f1 = np.polyfit(voltage, dp, 1)
ap1 = np.poly1d(f1)
plt.plot(x_calibr, ap1(x_calibr))
plt.minorticks_on()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
axis_lw = 2
ax1 = plt.gca()
plt.minorticks_on()
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
#plt.grid(visible=True, which='minor', linestyle='-.', linewidth=1.5, color='0.7')
ax1.set_xlabel('U, В')
ax1.set_ylabel('H, мм')
ax1.set_title('Соответствие уровня воды в кювете и напряжения')



# глубина от времени
fig2, ax2 = plt.subplots()
plt.plot(t40, d40)
plt.axvline(wvtm40, color = 'red', linestyle = '-.', label = 't_40 = 2.06 с')
ax2 = plt.gca()
plt.grid(visible=True, which='minor', linestyle='-.', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
ax2.set_xlabel('t, с')
ax2.set_ylabel('H, мм')
ax2.set_title('h = 40 мм')
ax2.text(3, 2, 'V40 = 0.48 м/с')
ax2.legend()

fig3, ax3 = plt.subplots()
plt.plot(t80, d80)
plt.axvline(wvtm80, color = 'red', linestyle = '-.', label = 't_80 = 1.48 с')
ax3 = plt.gca()
plt.grid(visible=True, which='minor', linestyle='-.', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
ax3.set_xlabel('t, с')
ax3.set_ylabel('H, мм')
ax3.set_title('h = 80 мм')
ax3.text(3, 2, 'V80 = 0.93 м/с')
ax3.legend()


fig4, ax4 = plt.subplots()
plt.plot(t120, d120)
plt.axvline(wvtm120, color = 'red', linestyle = '-.', label = 't_120 = 0.96 с')
ax4 = plt.gca()
plt.grid(visible=True, which='minor', linestyle='-.', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
ax4.set_xlabel('t, с')
ax4.set_ylabel('H, мм')
ax4.set_title('h = 120 мм')
ax4.text(3, 20, 'V120 = 2.21 м/с')
ax4.legend()

# скорость от глубины
fig5, ax5 = plt.subplots()
plt.plot(h_tst, sp_tst)
h_rl = [0.04, 0.08, 0.12]
sp_rl = [sp40, sp80, sp120]
plt.scatter(h_rl, sp_rl)
ax5 = plt.gca()
plt.grid(visible=True, which='minor', linestyle='-.', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')



plt.show()
