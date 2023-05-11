import json
import numpy as np
import os

import matplotlib.pyplot as plt

plt.style.use('/home/liam/Documents/bees-sensor-2023/analysis/print.mplstyle')

log_path = "/home/liam/Documents/bees-sensor-2023/analysis/data/23-04-02.log"
line_num = 600

with open(log_path) as fp:
    
    for idx, line in enumerate(fp.readlines()):
        if idx != 600:
            continue
        items = line.split(':')
        pixels = np.asarray(json.loads(items[1]))
        average_temp = np.average(pixels)

        pixels = np.rot90(pixels, 3)
        # print(len(pixels[0]), "x", len(pixels))


        grid_x, grid_y = np.mgrid[0:31:32j, 0:23:24j]

        plt.figure()
        plt.pcolormesh(grid_x, grid_y, pixels)
        cbar = plt.colorbar()
        cbar.set_label("Temperature (\u00b0C)")
        # plt.title(f'temp (avg): {average_temp}')

        fig = plt.gcf()
        fig.set_dpi(300)
        fig.set_size_inches(4.25, 4.5)

        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.tight_layout()
        plt.savefig(f'out.png', format='png')

        plt.close()