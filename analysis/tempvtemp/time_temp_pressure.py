import common
import os
import matplotlib.pyplot as plt
import matplotlib as mpl

timestamp, average_temp, outside_temp, humidity, pressure = common.process_data()

cbar = common.plot_color(pressure,
                  average_temp,
                  norm=(0, 86400),
                  c_variable=timestamp,
                  cbar_label="Time of Day")

common.set_limits_and_labels("Air Pressure (hPa)",
                             "Average Camera Temperature (\u00b0C)",
                             None,
                             (-15, 50))

common.trendline(pressure, average_temp)

ax = plt.gca()

ticks = [0, 3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800, 32400, 36000, 39600, 43200, 46800, 50400, 54000, 57600, 61200, 64800, 68400, 72000, 75600, 79200, 82800, 86400]
labels = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]

cbar.set_ticks(ticks)
cbar.set_ticklabels(labels)


common.size_and_save(__file__)