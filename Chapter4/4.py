#Scalar and Vector Magnetic Potentials:

import numpy as np

class ScalarMagneticPotential:
    def __init__(self, current, r_vector):
        self.current = current
        self.r_vector = r_vector

    def scalar_potential(self):
        r = np.linalg.norm(self.r_vector)
        return (1e-7 * self.current) / (4 * np.pi * r)

class VectorMagneticPotential:
    def __init__(self, current, r_vector):
        self.current = current
        self.r_vector = r_vector

    def vector_potential(self):
        r = np.linalg.norm(self.r_vector)
        return (1e-7 * self.current) / (4 * np.pi * r**2) * np.cross(r_vector, [0, 0, 1])

# Example usage:
current = 5  # Amperes
r_vector = np.array([1, 2, 3])
scalar_potential = ScalarMagneticPotential(current, r_vector).scalar_potential()
vector_potential = VectorMagneticPotential(current, r_vector).vector_potential()
print("Scalar Magnetic Potential (Amps):", scalar_potential)
print("Vector Magnetic Potential (Amps/m):", vector_potential)
