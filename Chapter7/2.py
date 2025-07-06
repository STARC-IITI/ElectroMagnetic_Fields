#Skin Depth
import numpy as np

# Constants
f = 1e9  # Frequency in Hz (e.g., 1 GHz)
mu = 4 * np.pi * 1e-7  # Permeability of free space in H/m
sigma = 5.8e7  # Electrical conductivity of the conductor in S/m
omega = 2 * np.pi * f  # Angular frequency

# Calculate skin depth (delta) for a good conductor
delta = np.sqrt(2 / (mu * sigma * omega))

# Print the calculated skin depth
print(f"Skin Depth (delta): {delta} meters")
