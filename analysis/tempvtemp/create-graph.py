import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('tempvtemp.log', delimiter=":")
average_max, outside_max = data.max(axis=0)
# with open('tempvtemp.log') as fp:
#     average_array, outside_array = [], []

#     for line in fp.readlines():
#         average, outside = line.split(':')
#         average_array.append(float(average))
#         outside_array.append(float(outside))
    
#     x = np.array(average_array)
#     y = np.array(outside_array)

#     plt.scatter(x, y)
#     plt.savefig('out.jpg', format='jpg')
