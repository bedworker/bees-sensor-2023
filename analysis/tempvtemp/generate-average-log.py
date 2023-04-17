import json
import numpy as np
import os

from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data_folder_path = "/home/liam/Documents/bees-sensor-2023/analysis/data"

logs = [
    f'{data_folder_path}/{log}'
    for log in [
        file 
        for file in os.listdir(data_folder_path) 
        if '.log' in file
        ]
    ]

with open('./tempvtemp.log', 'a') as outlog:
    for log in logs:
        with open(log) as fp:
            lines = []

            for idx, line in enumerate(fp.readlines()):
                # if idx % 60 != 0:
                #     continue
                items = line.split(':')
                pixels = np.asarray(json.loads(items[1]))
                outside_temp = items[3]
                average_temp = np.average(pixels)
                if average_temp > 100:
                    print(idx, log)

                lines.append(f'{average_temp}:{outside_temp}\n')

            # outlog.writelines(lines)