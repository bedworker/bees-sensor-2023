import os
import json

import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=5)

x = np.array([" "])
y = np.array([1])
ax1.bar(x, y)
ax1.set_ylim(0,10)
ax2.bar(x, np.array([30]))
ax2.set_ylim(0,20)
plt.show()