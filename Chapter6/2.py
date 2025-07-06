#Displacement Current
import sympy as sp

# Define symbolic variables
J_d, epsilon_0, dE_dt = sp.symbols('J_d epsilon_0 dE_dt')

# Define the formula for displacement current
displacement_current = sp.Eq(J_d, epsilon_0 * dE_dt)

# Assuming some values for epsilon_0 and the rate of change of electric field (dE/dt)
epsilon_0_value = 8.854187817e-12  # Vacuum permittivity in F/m
dE_dt_value = 2.0  # Example rate of change of electric field in V/m/s

# Calculate the displacement current
displacement_current_value = displacement_current.subs({epsilon_0: epsilon_0_value, dE_dt: dE_dt_value})

# Print the displacement current
print("Displacement Current (J_d):")
sp.pprint(displacement_current_value)
