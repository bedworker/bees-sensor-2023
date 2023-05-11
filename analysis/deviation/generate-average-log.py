import json
import numpy as np
import os
from tqdm import tqdm

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

with open('./tempvtemp.log', 'w') as outlog:
    for log_idx, log in enumerate(tqdm(logs)):
        with open(log) as fp:
            outlines = []
            lines = fp.readlines()

            for line_idx, line in enumerate(lines):
                items = line.split(':')
                pixels = np.asarray(json.loads(items[1]))
                outside_temp = items[3]

                average_temp = np.average(pixels)

                difference =  float(average_temp) - float(outside_temp)

                outlines.append(f'{int(items[0])}:{difference}\n')
                # print(f'line {line_idx + 1} of {len(lines)}, in log {os.path.basename(log)} ({log_idx + 1} of {len(logs)})')

            outlog.writelines(outlines)