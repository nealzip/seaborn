__author__ = 'nealzipper'
# User: nealzipper
# Date: 4/2/17
# Time: 11:22 PM
# Project Name: seaborn
# Copyright 2017 Neal Zipper

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("darkgrid")
plt.plot(np.cumsum(np.random.randn(1000,1)))
plt.show()
