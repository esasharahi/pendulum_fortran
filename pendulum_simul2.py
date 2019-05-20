import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
##
##
data1 = np.loadtxt('pendulum.txt')
x = np.sin(data1[:,1])
y = - np.cos(data1[:,1])
##
##
fig, ax = plt.subplots()
x_fix, y_fix = 0, 0
xdata, ydata = x[0], y[0]
ln, = plt.plot([], [], 'ro-', animated = True)
plt.plot([x_fix], [y_fix], 'bo', ms = 10)

def init():
    ax.set_xlim(np.amin(x) - 1, np.amax(x) + 1) 
    ax.set_ylim(np.amin(y) - 1, np.amax(y) + 1)
    return ln,

def update(frame):
    xdata = x[frame]
    ydata = y[frame]
    ln.set_data([x_fix,xdata], [y_fix,ydata])
    return ln,          


ani = FuncAnimation(fig, update, frames = range(len(x)),
            init_func = init, blit = True)
plt.show()
