import json
import numpy as np

from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('data/23-03-18.log') as fp:
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

        plt.savefig(f'out/{idx}.jpg', format='jpg')

        plt.close()