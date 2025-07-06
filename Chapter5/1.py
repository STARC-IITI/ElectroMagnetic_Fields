import numpy as np

class MagneticForce:
    def __init__(self, charge, velocity, magnetic_field):
        self.charge = charge
        self.velocity = velocity
        self.magnetic_field = magnetic_field

    def calculate_force_on_charge(self):
        # Calculate the force on a moving charge due to the magnetic field
        # Using the Lorentz force formula: F = q * (v x B)
        force = np.cross(self.charge * self.velocity, self.magnetic_field)
        return force

# Example usage:
# Charge moving in a magnetic field
charge = 1.6e-19  # Charge of an electron in Coulombs
velocity = np.array([0, 1, 0])  # Velocity of the charge in m/s
magnetic_field = np.array([0, 0, 1])  # Magnetic field in Tesla

charge_force_calculator = MagneticForce(charge, velocity, magnetic_field)
charge_resulting_force = charge_force_calculator.calculate_force_on_charge()

print("Force on the moving charge (N):", charge_resulting_force)
