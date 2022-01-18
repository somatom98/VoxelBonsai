import math
import sys
import coloredlogs
from pyvox.parser import VoxParser

coloredlogs.install(level='DEBUG')

m = VoxParser(sys.argv[1]).parse()

img = m.to_dense()

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

cm = ListedColormap(np.array(m.palette, dtype='f')/256)

s = math.ceil(math.sqrt(img.shape[0]))
print('size', img.shape, s)
f, arr = plt.subplots(s,s)
for i, slc in enumerate(img):
    arr[i//s, i%s].imshow(img[i], cmap=cm)
for a in range(i+1, s*s):
    arr[a//s, a%s].imshow(np.zeros(img.shape[1:3]))

plt.show()
