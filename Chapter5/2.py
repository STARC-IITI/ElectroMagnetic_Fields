import numpy as np

class MagneticMaterial:
    def __init__(self, susceptibility, external_field):
        self.susceptibility = susceptibility  # Magnetic susceptibility
        self.external_field = external_field  # External magnetic field

    def calculate_magnetization(self):
        # Calculate the magnetization of the material
        magnetization = self.susceptibility * self.external_field
        return magnetization

    def calculate_permeability(self):
        # Calculate the permeability of the material
        permeability = (1 + self.susceptibility) * 4 * np.pi * 1e-7  # Permeability of free space
        return permeability

# Example usage:
susceptibility = 0.01  # Magnetic susceptibility of the material
external_field = 0.2  # External magnetic field in Tesla

material = MagneticMaterial(susceptibility, external_field)

magnetization = material.calculate_magnetization()
permeability = material.calculate_permeability()

print("Magnetization (A/m):", magnetization)
print("Permeability (H/m):", permeability)
