import numpy as np
import matplotlib.pyplot as plt

data40 = np.loadtxt("/home/b03-303/privetyasobaka/data_120_2.txt", delimiter='\t', dtype=np.float)
x_1 = np.linspace(0, len(data40), len(data40))
plt.plot(x_1, data40)
plt.show()

