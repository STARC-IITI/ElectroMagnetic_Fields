#Magnetic Flux:

import numpy as np

class MagneticFlux:
    def __init__(self, magnetic_field, area_vector):
        self.magnetic_field = magnetic_field
        self.area_vector = area_vector

    def flux(self):
        return np.dot(self.magnetic_field, self.area_vector)

# Example:
magnetic_field = np.array([0.1, 0.2, 0.3])
area_vector = np.array([1, 2, 3])
magnetic_flux = MagneticFlux(magnetic_field, area_vector)
flux_value = magnetic_flux.flux()
print("Magnetic Flux (Weber):", flux_value)
