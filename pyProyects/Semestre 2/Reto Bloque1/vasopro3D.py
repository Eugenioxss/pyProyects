#Etapa3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

n = 501 # Number of points to plot and complete domain: [0, 9.5]
x1 = np.linspace(0, 9.5, n)
y1 = 0.00025*x1**4 - 0.012*x1**3 + 0.2*x1**2 - 1.291*x1 - 2.06      # Original shape

#Elements considered for the inner face of the glass
base = .5
thickness = .3
x2 = x1[x1>=base]
y2 = 0.00025*x2**4 - 0.012*x2**3 + 0.2*x2**2 - 1.291*x2 - 2.06 - thickness

# Plotting positive values
plt.plot(x1, y1, color='r')
#plt.plot(x2, y2, color='b')
# Plotting negative values (just for symmetry)
plt.plot(x1, -y1, color='r')
#plt.plot(x2, -y2, color='b')


# Graph settings
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122,projection='3d')

# Our rotation vector. It goes from 0 to 2pi for a full rotation.
t = np.linspace(0, np.pi*2, n)

# Outer products with rotation
xn = np.outer(y1, np.sin(t))
yn = np.outer(y1, np.cos(t))

# Generate a zero matrix with the same size as xn
zn = np.zeros_like(yn)

# Now, create a mesh by adding all points in each line to be something like (of the same dimension) as the combination of z and y
for i in range(len(x1)):
    zn[i:i+1,:] = np.full_like(zn[0,:], x1[i])

# Plot the function and reflection
ax1.plot(y1, x1)
ax1.plot(-y1,x1)
ax1.plot(y2, x2)
ax1.plot(-y2,x2)

# And a little line on x = 0 to be fancier
ax1.vlines(0,0,10,linestyle="--", color="r")
ax1.set_xlim([-max(y1),max(y1)])

# Now plot the 3D Surface!
ax2.plot_surface(yn, xn, zn)

# Volume = pi * Area
vol1 = np.pi * np.trapz(y1, x1)
vol2 = np.pi * np.trapz(y2, x2)

# Total volume
print('Total volume: ', vol1)

plt.show()

"""
#Etapa3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

n = 501 # Number of points to plot and complete domain: [0, 20]
x = np.linspace(0, 20, n)

# Functions to be plotted piecewise
x1 = x[x <= .9]                                 # [0,1)
x2 = x[np.logical_and(x >= .9, x <= 10)]         # [1,10)
x3 = x[x > 10]                                 # [10, 20]

y1 = -5*x1+5
y2 = [.5] * len(x2)
y3 = 10**.75 / 2 * (x3-10) ** .25
y = np.concatenate([y1, y2, y3])

# Inner part of the glass
x4 = x[x >= 11]
y4 = (9)**.75 / 2 * (x4-11) ** .25

# Plotting positive values (upper half)
plt.plot(x, y)
plt.plot(x4, y4)

# Plotting negative values (upper half)
plt.plot(x, -y)
plt.plot(x4, -y4)

# Graph settings
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122,projection='3d')

# Our rotation vector. It goes from 0 to 2pi for a full rotation.
t = np.linspace(0, np.pi*2, n)

# Outer products with rotation
xn = np.outer(y, np.sin(t))
yn = np.outer(y, np.cos(t))

# Generate a zero matrix with the same size as xn
zn = np.zeros_like(yn)

# Now, create a mesh by adding all points in each line to be something like (of the same dimension) as the combination of z and y
for i in range(len(x)):
    zn[i:i+1,:] = np.full_like(zn[0,:], x[i])

# Plot the function and reflection
ax1.plot(y, x)
ax1.plot(-y,x)
ax1.plot(y4, x4)
ax1.plot(-y4,x4)

# And a little line on x = 0 to be fancier
ax1.vlines(0,0,10,linestyle="--", color="r")
ax1.set_xlim([-max(y),max(y)])

# Now plot the 3D Surface!
ax2.plot_surface(yn, xn, zn)
plt.show()

# Volume = pi * Area
vol1 = np.pi * np.trapz(y, x)
vol2 = np.pi * np.trapz(y4, x4)

# Total volume
print('Total volume: ', vol1 - vol2)

# Graph settings
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122,projection='3d')

# Our rotation vector. It goes from 0 to 2pi for a full rotation.
t = np.linspace(0, np.pi*2, n)

# Outer products with rotation
xn = np.outer(y, np.sin(t))
yn = np.outer(y, np.cos(t))

# Generate a zero matrix with the same size as xn
zn = np.zeros_like(yn)

# Now, create a mesh by adding all points in each line to be something like (of the same dimension) as the combination of z and y
for i in range(len(x)):
    zn[i:i+1,:] = np.full_like(zn[0,:], x[i])

# Plot the function and reflection
ax1.plot(y, x)
ax1.plot(-y,x)
ax1.plot(y4, x4)
ax1.plot(-y4,x4)

# And a little line on x = 0 to be fancier
ax1.vlines(0,0,10,linestyle="--", color="r")
ax1.set_xlim([-max(y),max(y)])

# Now plot the 3D Surface!
ax2.plot_surface(yn, xn, zn)
plt.show()

# Volume = pi * Area
vol1 = np.pi * np.trapz(y, x)
vol2 = np.pi * np.trapz(y4, x4)

# Total volume
print('Total volume: ', vol1 - vol2)

"""

