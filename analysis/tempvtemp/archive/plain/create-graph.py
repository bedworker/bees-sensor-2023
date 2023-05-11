import matplotlib.pyplot as plt
import numpy as np

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/print.mplstyle')

data = np.genfromtxt('tempvtemp.log', delimiter=":")
average_max, outside_max = data.max(axis=0)
x = data[:, 1] # outside temp
y = data[:, 0] # average temp

data = data[y < 150]
a, b = np.polyfit(x, y, 1)
print(a, b)
plt.scatter(x, y, s=0.05, c="black")
plt.plot(x, a*x + b, c="red")
plt.xlabel("Outside Temperature (°C)")
plt.ylabel("Average Camera Temperature (°C)")

ax = plt.gca()
ax.set_xlim(-15, 50)
ax.set_ylim(-15, 50)

# change size of plot so it fits
fig = plt.gcf()
fig.set_size_inches(7,6)
fig.set_dpi(300)

plt.tight_layout()
plt.savefig('out.png', format='png')