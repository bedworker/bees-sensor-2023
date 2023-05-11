import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
import pytz

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/print.mplstyle')


data = np.genfromtxt('tempvtemp.log', delimiter=":")
average_max, outside_max = data.max(axis=0)
data = data[data[:, 1] < 150] # filter out average temperatures of more than 150°C

ax = plt.gca()
# ax.set_xlim(950, 985)
ax.set_ylim(-15, 50)

a, b = np.polyfit(data[:, 1], data[:, 2], 1)
plt.plot(data[:, 1], a * data[:, 1] + b)
ax.annotate(f'Trendline: y = {round(a, 2)}x + {round(b,2)}',
            (950,48),
            c='black',
            size=12)
cbar = plt.colorbar()
cbar.set_label("Time of Day (seconds)")


plt.scatter(data[:, 0], data[:, 1], s=0.05, c="black")
plt.xlabel("Air Pressure (hPa)")
plt.ylabel("Average Camera Temperature (°C)")
 

# change size of plot so it fits
fig = plt.gcf()
fig.set_size_inches(7,6)
fig.set_dpi(300)

plt.tight_layout()
plt.savefig('out-color.png', format='png')