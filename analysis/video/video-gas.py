import os
import json

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/style.mplstyle')

def get_min_max(log_list):
    array = np.empty((1, 7))

    for log in log_list:
        array = np.concatenate((array, np.genfromtxt(log, delimiter=":")))
    
    array = array[:,3:] # filter to only the right 4 columns
    
    min_list = np.min(array, axis=0)
    max_list = np.max(array, axis=0)

    return min_list, max_list

    # print(array)
    
def make_bar(ax: plt.Axes, title: str, data):
    # print(data)
    ax.bar(blank, np.array([data]))
    ax.set_ylabel(title)
    ax.set_xticklabels([])
    # ax.set_xticks([])
    

data_folder_path = "/home/liam/Documents/bees-sensor-2023/analysis/data"
out_folder_path = "/home/liam/Documents/bees-sensor-2023/analysis/video/frames/out"

logs = [
    f'{data_folder_path}/{log}'
    for log in [
        file 
        for file in os.listdir(data_folder_path) 
        if '.log' in file
        ]
    ]


# constants :)
interval = 60
standard_pressure = 1013.25 # earth standard pressure (1 atm)


try:
    os.mkdir(out_folder_path)
except FileExistsError:
    pass

for log in logs:
    with open(log) as fp:
        out_dirname = f'{out_folder_path}/{os.path.basename(log).replace(".log", "")}'
        try:
            os.mkdir(out_dirname)
        except FileExistsError:
            pass
        for idx, line in enumerate(fp.readlines()):
            if idx % interval != 0:
                continue
            items = line.split(':')
            pixels = np.asarray(json.loads(items[1]))
            average_temp = np.average(pixels)

            pixels = np.rot90(pixels, 3)
            # print(len(pixels[0]), "x", len(pixels))

            # constants
            grid_x, grid_y = np.mgrid[0:31:32j, 0:23:24j]
            blank = np.array([" "])

            # names
            timestamp = int(items[0])
            outside_temp = float(items[3])
            gas = float(items[4])
            humidity = float(items[5])
            pressure = float(items[6])

            # adjust pressure
            pressure = standard_pressure - pressure


            # make the plots
            fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows=1, ncols=6, gridspec_kw={"width_ratios": [15,1,1,1,1,1]})
            # 1: heatmap of camera data
            # 2: average temperature of camera (C)
            # 3: outside temperature (C)
            # 4: gas (ohms)
            # 5: humidity (percent)
            # 6: relative air pressure (hPa)
            norm = mpl.colors.Normalize(vmin=-15, vmax=50)
            ax2.set_ylim(-15, 50)
            ax3.set_ylim(-15, 50)
            ax4.set_ylim(0, 35000)
            ax5.set_ylim(0, 100)
            ax6.set_ylim(-100, 100)

            # heatmap from camera
            heatmap = ax1.pcolormesh(grid_x, grid_y, pixels, norm=norm)
            plt.colorbar(heatmap, ax=ax1, norm=norm)
            ax1.set_title("Heatmap")
            ax1.set_aspect('equal', adjustable='box')
            ax1.set_xticks([])
            ax1.set_yticks([])
            fig.text(0.05, 0.05, f't:{timestamp}', fontsize=20)

            # the other bars
            make_bar(ax2, "Average Heatmap Temp (\u00b0C)", average_temp)
            make_bar(ax3, "Outside Temp (\u00b0C)", outside_temp)
            make_bar(ax4, "Gas (\u2126)", gas)
            make_bar(ax5, "Relative Humidity (%)", humidity)
            make_bar(ax6, "Relative Air Pressure (hPa)", pressure)

            # adjust for no overlap
            plt.tight_layout(w_pad=-4)

            fig.set_size_inches(20, 10)
            # fig.set_facecolor('#34495e') # wet asphalt
            plt.savefig(f'{out_dirname}/{idx}.png', format='png')

            plt.close()
            # exit()
    exit()