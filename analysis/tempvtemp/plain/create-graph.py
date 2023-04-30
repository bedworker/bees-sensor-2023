import matplotlib.pyplot as plt
import numpy as np

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/print.mplstyle')

data = np.genfromtxt('tempvtemp.log', delimiter=":")
average_max, outside_max = data.max(axis=0)
data = data[data[:, 0] < 150]
plt.scatter(data[:, 1], data[:, 0], s=0.05, c="black")
plt.xlabel("Outside Temperature (°C)")
plt.ylabel("Average Camera Temperature (°C)")
plt.savefig('out.jpg', format='jpg')

# change size of plot so it fits
fig = plt.gcf()
fig.set_size_inches(7,6)
fig.set_dpi(150)

plt.tight_layout()
plt.savefig('out.png', format='png')