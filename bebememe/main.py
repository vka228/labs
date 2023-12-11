import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
def remove_nan(x):
    return [i for i in x if i == i]

def timar(x, tm):
    time = np.linspace(0, (len(x) - 1) * tm, len(x) )
    return time
def justify(a, invalid_val=0, axis=1, side='left'):
    if invalid_val is np.nan:
        mask = ~np.isnan(a)
    else:
        mask = a!=invalid_val
    justified_mask = np.sort(mask,axis=axis)
    if (side=='up') | (side=='left'):
        justified_mask = np.flip(justified_mask,axis=axis)
    out = np.full(a.shape, invalid_val)
    if axis==1:
        out[justified_mask] = a[mask]
    else:
        out.T[justified_mask.T] = a.T[mask.T]
    return out
# определяем время прихода волны
def wavetm(x):
    i = 0
    c1 = 0
    c2 = 0
    c3 = 0
    while abs(c1 - c2) < abs(c2 - c3) + 3:
        c1 = x[i]
        c2 = x[i + 1]
        c3 = x[i + 2]
        i += 1
    return i


# коэффицент наклона по мнк
def coef(k, v):
    sumv = 0
    sumn = 0
    sumvn = 0
    sumn_sq = 0
    rng = len(v)

    for i in range(rng):
        sumvn += v[i] * k[i]
        sumn += k[i]
        sumv += v[i]
        sumn_sq += int(k[i] ** 2)

    k = (rng * sumvn - sumn * sumv) / (rng * sumn_sq - (sumn) ** 2)
    return k


# b
def bmnk(x, y):
    sumx = 0
    sumy = 0
    rng = len(x)
    for i in range(rng):
        sumx += x[i]
        sumy += y[i]
    mnx = sumx / rng
    mny = sumy / rng

    b = mny - coef(x, y) * mnx
    return b

# перевод из массива напряжений в массив высот
def prv(a):
    for i in range (len(a) - 1):
        a[i] = 3.3 - ((a[i]) / 256 * 3.3)
    return a


# производим калибровку - задаём массив глубин воды и
# массивы напряжений
voltage = 3.3 - np.array([224.01, 198, 176.8, 159.12, 143.8, 127.3]) / 256 * 3.3
dp = np.array([20, 40, 60, 80, 100, 120])


x_calibr = np.linspace(0.25, voltage[5], 100)





xls = pd.ExcelFile(r"data.xlsx") # use r before absolute file path
data = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis
data[:] = justify(data.values, invalid_val=np.nan, axis=0, side='up')
data = data.fillna('')

# raw напряжения для разных начальных заполнений кюветы
d40 = np.loadtxt("data_40.txt", delimiter='\t')
d80 = np.loadtxt("data_80.txt", delimiter='\t')
d120 = np.loadtxt("data_120.txt", delimiter='\t')

d40 = 3.3 - d40 / 256 * 3.3
d80 = 3.3 - d80 / 256 * 3.3
d120 = 3.3 - d120 / 256 * 3.3

#d40 = d40 * 80 - 18.437
#d80 = d80 * 60 - 18.437
#d120 = d120 * 80 - 18.437

d40 = d40 * 81.25 - 17.25
d80 = d80 * 81.25 - 17.25
d120 = d120 * 81.25 - 17.25
#d40 = d40 * coef(dp, voltage) - bmnk(dp, voltage)
#d80 = d80 * coef(dp, voltage) - bmnk(dp, voltage)
#d120 = d120 * coef(dp, voltage) - bmnk(dp, voltage)







# для графика скорости от высоты
h_tst = np.linspace(0, 0.15, 100)
sp_tst = []
for i in range(len(h_tst)):
    sp_tst.append((h_tst[i] * 9.81))

# создаём массивы времён для каждого из заполнений кюветы
t40 = np.ndarray.tolist(timar(d40, 0.014))
t80 = np.ndarray.tolist(timar(d80, 0.02))
t120 = np.ndarray.tolist(timar(d120, 0.02))

wvtm40 = wavetm(d40) * 0.014
wvtm80 = wavetm(d80) * 0.02
wvtm120 = wavetm(d120) * 0.02
print(wvtm40, wvtm80, wvtm120)
'''sp40 = (1.43 / wvtm40)**2
sp80 = (1.43 / wvtm80) **2
sp120 = (1.43 / wvtm120) **2'''

sp40 = (1.43 / wvtm40)
sp80 = (1.43 / wvtm80)
sp120 = (1.43 / wvtm120)
print(sp40, sp80, sp120)



