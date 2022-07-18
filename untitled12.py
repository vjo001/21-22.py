# importing libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# defending surface and axes
x = np.outer(np.linspace(-10, 10, 10), np.ones(10))
y = x.copy().T
z = np.tan(x ** 2 + y ** 3)

fig = plt.figure()

# syntax for 3-D plotting
ax = plt.axes(projection ='3d')

# syntax for plotting
ax.plot_surface(x, y, z, cmap ='cool', edgecolor ='purple')
ax.set_title('Surface Plot')
plt.show()