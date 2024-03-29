import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
import pytz

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/style.mplstyle')


data = np.genfromtxt('tempvtemp.log', delimiter=":")
average_max, outside_max = data.max(axis=0)
data = data[data[:, 1] < 150] # filter out average temperatures of more than 150°C
# norm = mpl.colors.Normalize(0, 100)

plt.scatter(data[:, 0], data[:, 1], s=0.05)
plt.xlabel("Air Pressure (hPa)")
plt.ylabel("Average Camera Temperature (°C)")

# cbar = plt.colorbar()
# cbar.set_label("Relative Humidity (%)")

# change size of plot so it fits
fig = plt.gcf()
fig.set_size_inches(8,6)
fig.set_dpi(150)

plt.tight_layout()
plt.savefig('out-color.png', format='png')