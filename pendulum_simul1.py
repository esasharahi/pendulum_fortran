import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots()

data1 = np.loadtxt('pendulum.txt')

x = np.sin(data1[:,1])
y = - np.cos(data1[:,1])

for t in range(len(x) - 1):
    if t == 0:
        points, = ax.plot(x, y, marker='o', linestyle='None')
        ax.set_xlim(np.amin(x) - 1, np.amax(x) + 1) 
        ax.set_ylim(np.amin(y) - 1, np.amax(y) + 1) 
    else:
        new_x = x[t + 1]
        new_y = y[t + 1]
        points.set_data(new_x, new_y)
    plt.pause(0.1)
