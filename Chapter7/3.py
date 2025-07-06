#Poynting Vector
import numpy as np

# Constants
E = np.array([1.0, 0.0, 0.0])  # Electric field vector (V/m)
H = np.array([0.0, 0.0, 1.0])  # Magnetic field vector (A/m)
mu = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
epsilon = 8.854187817e-12  # Permittivity of free space (F/m)
c = 1 / np.sqrt(mu * epsilon)  # Speed of light (m/s)

# Calculate the Poynting vector
S = np.cross(E, H)  # Poynting vector (W/m^2)

# Calculate the energy density
u = 0.5 * (np.dot(E, E) / epsilon + np.dot(H, H) / mu)

# Calculate the time rate of change of energy density
dU_dt = -np.dot(S, np.array([1, 0, 0]))  # Considering a 1D scenario

# Display the results
print("Poynting Vector (S):", S)
print("Electromagnetic Energy Density (u):", u)
print("Time Rate of Change of Energy Density (dU/dt):", dU_dt)
