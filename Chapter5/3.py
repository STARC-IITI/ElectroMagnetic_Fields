import numpy as np

class Inductor:
    def __init__(self, turns, area, length, permeability):
        self.turns = turns  # Number of turns
        self.area = area  # Cross-sectional area
        self.length = length  # Length of the coil
        self.permeability = permeability  # Permeability of the medium

    def calculate_self_inductance(self):
        # Calculate the self-inductance of the coil
        self_inductance = (self.turns**2 * self.permeability * self.area) / self.length
        return self_inductance

    def calculate_mutual_inductance(self, other_coil):
        # Calculate the mutual inductance between two coils
        mutual_inductance = (self.turns * other_coil.turns * self.permeability * self.area) / (2 * np.pi * np.sqrt((self.length + other_coil.length) * self.length * other_coil.length))
        return mutual_inductance

# Example usage:
permeability_of_free_space = 4 * np.pi * 1e-7  # Permeability of free space (H/m)

# Define the first coil
coil1 = Inductor(turns=100, area=0.001, length=0.1, permeability=permeability_of_free_space)

# Define the second coil
coil2 = Inductor(turns=50, area=0.001, length=0.05, permeability=permeability_of_free_space)

self_inductance1 = coil1.calculate_self_inductance()
self_inductance2 = coil2.calculate_self_inductance()
mutual_inductance = coil1.calculate_mutual_inductance(coil2)

print("Self-Inductance of Coil 1 (H):", self_inductance1)
print("Self-Inductance of Coil 2 (H):", self_inductance2)
print("Mutual Inductance between Coil 1 and Coil 2 (H):", mutual_inductance)
