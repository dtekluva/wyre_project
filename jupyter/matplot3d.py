from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")

z_line = np.linspace(0, 30, 1000)
x_line = np.cos(z_line)
y_line = np.sin(z_line)
# plt.plot(z_line,x_line)
# plt.plot(z_line,y_line)
# plt.show()
ax.plot3D(z_line, x_line, y_line, 'gray')

z_points = 30 * np.random.random(100)
x_points = np.cos(z_points)  * np.random.randn(100)
y_points = np.sin(z_points) * np.random.randn(100)
ax.scatter3D(z_points, x_points, y_points, c=z_points, cmap='hsv')

plt.show()
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()