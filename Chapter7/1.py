import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
Lx = 10.0  # Length of the domain in the x-direction
Ly = 10.0  # Length of the domain in the y-direction
T = 2.0    # Total simulation time
c = 1.0    # Wave propagation speed
Nx = 100   # Number of spatial points in the x-direction
Ny = 100   # Number of spatial points in the y-direction
Nt = 500   # Number of time steps

# Discretization
dx = Lx / Nx
dy = Ly / Ny
dt = T / Nt

# Create arrays for the spatial and temporal grids
x = np.linspace(0, Lx, Nx + 1)
y = np.linspace(0, Ly, Ny + 1)
t = np.linspace(0, T, Nt + 1)

# Initialize arrays for the wave function
u = np.zeros((Nt + 1, Nx + 1, Ny + 1))

# Initial conditions (e.g., a Gaussian pulse)
x0, y0 = Lx / 2, Ly / 2
sigma = 1.0
u[0, :, :] = np.exp(-((x - x0) ** 2 + (y - y0) ** 2) / (2 * sigma ** 2))

# Time-stepping loop to solve the wave equation
for n in range(1, Nt + 1):
    for i in range(1, Nx):
        for j in range(1, Ny):
            u[n, i, j] = 2 * u[n - 1, i, j] - u[n - 2, i, j] + \
                        (c ** 2) * (dt ** 2) * (
                            (u[n - 1, i + 1, j] - 2 * u[n - 1, i, j] + u[n - 1, i - 1, j]) / (dx ** 2) +
                            (u[n - 1, i, j + 1] - 2 * u[n - 1, i, j] + u[n - 1, i, j - 1]) / (dy ** 2))

# Create a 3D plot of the wave evolution
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u[0, :, :])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Amplitude')
plt.title('2D Wave Equation Simulation')
plt.show()
