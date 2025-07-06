#Ampere's Law:

import numpy as np

class AmpereLaw:
    def __init__(self, closed_path, current):
        self.closed_path = closed_path
        self.current = current

    def magnetic_field(self):
        total_length = np.linalg.norm(np.diff(self.closed_path, axis=0))
        return 2e-7 * self.current / total_length

# Example :
closed_path = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0]])  # Simple rectangular loop
current = 5  # Amperes
ampere_law = AmpereLaw(closed_path, current)
magnetic_field = ampere_law.magnetic_field()
print("Magnetic Field (T):", magnetic_field)
