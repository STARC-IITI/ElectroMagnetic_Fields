##Coordinate System Conversions
import numpy as np

class Vector:
    def __init__(self, components):
        self.components = np.array(components)

    def __str__(self):
        return str(self.components)

    def to_cylindrical(self):
        x, y, z = self.components
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return Vector([r, theta, z])

    def to_spherical(self):
        x, y, z = self.components
        r = np.sqrt(x**2 + y**2 + z**2)
        theta = np.arctan2(y, x)
        phi = np.arccos(z / r)
        return Vector([r, theta, phi])

if __name__ == "__main__":
    vec_in_rectangular = Vector([3, 4, 5])

    # Coordinate system conversions
    vec_in_cylindrical = vec_in_rectangular.to_cylindrical()
    vec_in_spherical = vec_in_rectangular.to_spherical()

    print("Vector in Rectangular Coordinates:", vec_in_rectangular)
    print("Vector in Cylindrical Coordinates:", vec_in_cylindrical)
    print("Vector in Spherical Coordinates:", vec_in_spherical)
