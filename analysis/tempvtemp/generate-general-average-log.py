import json
import numpy as np
import os

import matplotlib.pyplot as plt
from tqdm import tqdm

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
    for log in tqdm(logs):
        with open(log) as fp:
            lines = []

            for idx, line in enumerate(fp.readlines()):
                # if idx % 60 != 0:
                #     continue
                items = line.split(':')
                
                timestamp = items[0]

                pixels = np.asarray(json.loads(items[1]))
                average_temp = np.average(pixels)
                if average_temp > 100:
                    print(idx, log)
                
                outside_temp = items[3]
                humidity = items[5]
                pressure = items[6]

                lines.append(f'{timestamp}:{average_temp}:{outside_temp}:{humidity}:{pressure.rstrip()}\n')

            outlog.writelines(lines)