import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
import pytz

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/style.mplstyle')

def to_time_of_day(column):
    out_column = np.empty_like(column)
    for idx, timestamp in enumerate(column):
        from_timestamp = datetime.fromtimestamp(timestamp, tz=pytz.timezone("America/Chicago"))
        real_date = from_timestamp.date()
        date = datetime(real_date.year, real_date.month, real_date.day)
        time_of_day = timestamp - date.timestamp()

        out_column[idx] = time_of_day

        # print(time_of_day)

        # exit()
    return out_column
        


        


data = np.genfromtxt('tempvtemp.log', delimiter=":")
_, average_max, outside_max = data.max(axis=0)
data = data[data[:, 1] < 150] # filter out average temperatures of more than 150°C
data[:, 0] = to_time_of_day(data[:, 0])
norm = mpl.colors.Normalize(0, 86400)

plt.scatter(data[:, 2], data[:, 1], s=0.05, c=data[:, 0], norm=norm)
plt.xlabel("Outside Temperature (°C)")
plt.ylabel("Average Camera Temperature (°C)")

cbar = plt.colorbar()
cbar.set_label("Time of Day (seconds)")

# change size of plot so it fits
fig = plt.gcf()
fig.set_size_inches(8,6)
fig.set_dpi(150)

plt.tight_layout()
plt.savefig('out-color.png', format='png')