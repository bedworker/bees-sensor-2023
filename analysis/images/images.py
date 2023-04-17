import json
import numpy as np
import os

from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data_folder_path = "/home/liam/Documents/bees-sensor-2023/analysis/data"
out_folder_path = "/home/liam/Documents/bees-sensor-2023/analysis/images/out"

logs = [
    f'{data_folder_path}/{log}'
    for log in [
        file 
        for file in os.listdir(data_folder_path) 
        if '.log' in file
        ]
    ]

for log in logs:
    with open(log) as fp:
        out_dirname = f'{out_folder_path}/{os.path.basename(log).replace(".log", "")}'
        os.mkdir(out_dirname)
        for idx, line in enumerate(fp.readlines()):
            if idx % 60 != 0:
                continue
            items = line.split(':')
            pixels = np.asarray(json.loads(items[1]))
            average_temp = np.average(pixels)

            pixels = np.rot90(pixels, 3)
            # print(len(pixels[0]), "x", len(pixels))


            grid_x, grid_y = np.mgrid[0:31:32j, 0:23:24j]

            plt.figure()
            plt.pcolormesh(grid_x, grid_y, pixels)
            plt.colorbar()
            plt.title(f'temp (avg): {average_temp}')

            plt.savefig(f'{out_dirname}/{idx}.jpg', format='jpg')

            plt.close()