## esasharahi@gmail.com
#!/usr/bin/python
import os
import numpy as np  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig2d = plt.figure()

data1 = np.loadtxt('pendulum.txt')

ax = fig2d.add_subplot(1, 1, 1)
ax.plot(data1[:,0], data1[:,1], c = 'red', label = '$y$')
leg = ax.legend()
ax.set_title("RG4-pendulum equation $\mathrm{d}^2y / \mathrm{d}t^2 = - \dfrac{g}{l} \sin(y)$")
ax.set_xlabel('$t$')
ax.set_ylabel('$y$')





plt.show()
