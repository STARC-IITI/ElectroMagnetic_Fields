# Function to calculate electric field due to a dipole at the equatorial position

import numpy as np
import matplotlib.pyplot as plt

# Constants
k_e = 8.987e9

def electric_field_at_equator(q1, q2, r):
    electric_field = (1 / (4 * np.pi * k_e)) * ((q1 - q2) / r**3)
    return electric_field


q1 = 1e-19
q2 = -1e-19
distances = np.linspace(0.01, 0.1, 100)


electric_fields = [electric_field_at_equator(q1, q2, r) for r in distances]

# Plot the electric field as a function of distance
plt.figure(figsize=(8, 4))
plt.plot(distances, electric_fields, color='b', linestyle='-')
plt.xlabel('Distance from Dipole Center (meters)')
plt.ylabel('Electric Field at Equatorial Position (N/C)')
plt.title('Electric Field of a Dipole at Equatorial Position')
plt.grid(True)
plt.show()
