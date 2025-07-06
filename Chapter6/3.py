#Motional Electromotive Force
import sympy as sp

# Define symbolic variables
E, B, v, L, theta = sp.symbols('E B v L theta')

# Define the formula for motional emf
motional_emf = sp.Eq(E, B * v * L * sp.sin(theta))

# Assuming values for the variables
B_value = 0.2  # Magnetic field strength in T
v_value = 5.0  # Velocity of the conductor in m/s
L_value = 10.0  # Length of the conductor in meters
theta_value = sp.pi / 6  # Angle in radians (30 degrees)

# Calculate the motional emf
motional_emf_value = motional_emf.subs({B: B_value, v: v_value, L: L_value, theta: theta_value})

# Print the motional emf
print("Motional Electromotive Force (emf):")
sp.pprint(motional_emf_value)


