#Vector Calculus
import numpy as np
import sympy as sp

class Vector:
    def __init__(self, components):
        self.components = sp.Matrix(components)

    def gradient(self):
        gradient_x = sp.diff(self.components[0], sp.symbols('x'))
        gradient_y = sp.diff(self.components[1], sp.symbols('y'))
        gradient_z = sp.diff(self.components[2], sp.symbols('z'))
        return Vector([gradient_x, gradient_y, gradient_z])

    def divergence(self):
        divergence = sp.diff(self.components[0], sp.symbols('x')) + sp.diff(self.components[1], sp.symbols('y')) + sp.diff(self.components[2], sp.symbols('z'))
        return divergence

    def curl(self):
        curl_x = sp.diff(self.components[2], sp.symbols('y')) - sp.diff(self.components[1], sp.symbols('z'))
        curl_y = sp.diff(self.components[0], sp.symbols('z')) - sp.diff(self.components[2], sp.symbols('x'))
        curl_z = sp.diff(self.components[1], sp.symbols('x')) - sp.diff(self.components[0], sp.symbols('y'))
        return Vector([curl_x, curl_y, curl_z])

if __name__ == "__main__":
    # Define symbolic variables x, y, and z
    x, y, z = sp.symbols('x y z')

    vec = Vector([x, y, z])

    # Vector calculus operations
    gradient = vec.gradient()
    divergence = vec.divergence()
    curl = vec.curl()

    # Display the results
    print("Original Vector:", vec.components)
    print("Gradient:", gradient.components)
    print("Divergence:", divergence)
    print("Curl:", curl.components)
