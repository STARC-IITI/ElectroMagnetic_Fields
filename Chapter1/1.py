#Vector Algebra Operations
import numpy as np

class Vector:
    def __init__(self, components):
        self.components = np.array(components)

    def __str__(self):
        return str(self.components)

    def addition(self, other_vector):
        result = self.components + other_vector.components
        return Vector(result)

    def subtraction(self, other_vector):
        result = self.components - other_vector.components
        return Vector(result)

    def scalar_multiplication(self, scalar):
        result = self.components * scalar
        return Vector(result)

    def dot_product(self, other_vector):
        result = np.dot(self.components, other_vector.components)
        return result

    def cross_product(self, other_vector):
        result = np.cross(self.components, other_vector.components)
        return Vector(result)

if __name__ == "__main__":
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])

    # Vector algebra operations
    result_addition = vec1.addition(vec2)
    result_subtraction = vec1.subtraction(vec2)
    scalar = 2
    result_scalar = vec1.scalar_multiplication(scalar)
    dot_product = vec1.dot_product(vec2)
    cross_product = vec1.cross_product(vec2)

    print("Vector 1:", vec1)
    print("Vector 2:", vec2)
    print("Vector Addition:", result_addition)
    print("Vector Subtraction:", result_subtraction)
    print("Scalar Multiplication:", result_scalar)
    print("Dot Product:", dot_product)
    print("Cross Product:", cross_product)

