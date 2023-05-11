import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
import pytz

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/print.mplstyle')


data = np.genfromtxt('tempvtemp.log', delimiter=":")
# filter out the outliers
data = data[data[:, 1] < 150]

plt.scatter(data[:, 0], data[:, 1], s=0.05)
plt.xlabel("Time")
plt.ylabel("Temperature Difference (\u00b0C)")

# change size of plot so it fits
fig = plt.gcf()
fig.set_size_inches(7,6)
fig.set_dpi(300)

ax = plt.gca()
ax.get_xaxis().set_ticks([])

plt.tight_layout()
plt.savefig('out-color.png', format='png')