#Biot-Savart Law:

import numpy as np

class BiotSavartLaw:
    def __init__(self, current, r_vector, dl_vector):
        self.current = current
        self.r_vector = r_vector
        self.dl_vector = dl_vector

    def magnetic_field(self):
        r = np.linalg.norm(self.r_vector)
        cross_product = np.cross(self.dl_vector, self.r_vector)
        return (1e-7 * self.current / (4 * np.pi)) * cross_product / r**3

# Example usage:
current = 5  # Amperes
r_vector = np.array([1, 2, 3])
dl_vector = np.array([0.1, 0.2, 0.3])
biot_savart = BiotSavartLaw(current, r_vector, dl_vector)
magnetic_field = biot_savart.magnetic_field()
print("Magnetic Field (T):", magnetic_field)
