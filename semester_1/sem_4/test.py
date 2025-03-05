import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

x_measured = [1.01, 2.59, 3.03, 5.40, 7.33]
y_measured = [0.41, 0.84, 1.11, 3.22, 5.00]

x = [0.5, 9.0]
y = np.interp(x, x_measured, y_measured)

ax1.scatter(x_measured, y_measured, marker='x')

ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')

ax1.plot(x,y, 'r')

ax1.grid()

plt.show()
