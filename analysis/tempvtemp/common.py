import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
import pytz
import os

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/print.mplstyle')


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
        
def process_data(time_of_day: bool = True, filter_averages = True):
    data = np.genfromtxt('tempvtemp.log', delimiter=":")

    if filter_averages: data = data[data[:, 1] < 150] # filter out average temperatures of more than 150°C
    if time_of_day: data[:, 0] = to_time_of_day(data[:, 0])

    timestamp = data[:, 0]
    average_temp = data[:, 1]
    outside_temp = data[:, 2]
    humidity = data[:, 3]
    pressure = data[:, 4]

    return timestamp, average_temp, outside_temp, humidity, pressure

def plot_color(x, y, norm: tuple, c_variable, cbar_label: str, cmap: str = "plasma", s: float = 0.05):
    norm = mpl.colors.Normalize(norm[0], norm[1])
    plt.scatter(x, y, s=s, c=c_variable, norm=norm, cmap=cmap)
    ax = plt.gca()
    cbar = plt.colorbar(ax=ax)
    cbar.set_label(cbar_label)
    return cbar

def plot(x, y, s: float = 0.05):
    plt.scatter(x, y, s=s)

def set_limits_and_labels(x_label: str, y_label: str, x_lims: tuple = None, y_lims: tuple = None):
    ax = plt.gca()
    if x_lims != None: ax.set_xlim(x_lims[0], x_lims[1])
    if y_lims != None: ax.set_ylim(y_lims[0], y_lims[1])

    plt.xlabel(x_label)
    plt.ylabel(y_label)


def trendline(x, y, color: str = "black", degree: int = 1):
    ax = plt.gca()
    a, b = np.polyfit(x, y, degree)
    plt.plot(x, a*x + b, c=color)
    ax.text(0.01,
            0.99,
            f'Trendline: y = {round(a, 2)}x + {round(b,2)}',
            ha='left',
            va='top',
            c=color,
            transform=ax.transAxes,
            size=12)

def size_and_save(generator_file_path: str, size: tuple = (7,6), dpi: int = 300, filename: str = "out-color.png"):
    # change size of plot so it fits
    fig = plt.gcf()
    fig.set_size_inches(size[0], size[1])
    fig.set_dpi(dpi)

    dirname = os.path.dirname(generator_file_path)
    out_relative_path = f'{dirname}/out'

    if not os.path.exists(out_relative_path):
        os.mkdir(out_relative_path)
    
    file_location = f'{out_relative_path}/{os.path.basename(generator_file_path).removesuffix(".py")}'

    if not os.path.exists(file_location):
        os.mkdir(file_location)

    plt.tight_layout()
    plt.savefig(f'{file_location}/{filename}', format='png')











