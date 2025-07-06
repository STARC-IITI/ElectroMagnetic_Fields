# Maxwell's equations
import sympy as sp

# Define symbolic variables
rho, J_x, J_y, J_z, E_x, E_y, E_z, B_x, B_y, B_z, t = sp.symbols(
    'rho J_x J_y J_z E_x E_y E_z B_x B_y B_z t')

# Define constant values for physical constants
epsilon_0 = 8.854187817e-12  # Vacuum permittivity in F/m
mu_0 = 4 * sp.pi * 1e-7  # Permeability of free space in H/m

# Define the values of electric field and other quantities
rho_value = 1.0e-6  # Example value for charge density in C/m^3
J_x_value = 1.0e-2  # Example value for x-component of current density in A/m^2
J_y_value = 2.0e-2  # Example value for y-component of current density in A/m^2
J_z_value = 3.0e-2  # Example value for z-component of current density in A/m^2
E_x_value = 100.0  # Example value for x-component of electric field in V/m
E_y_value = 200.0  # Example value for y-component of electric field in V/m
E_z_value = 300.0  # Example value for z-component of electric field in V/m
B_x_value = 0.1  # Example value for x-component of magnetic field in T
B_y_value = 0.2  # Example value for y-component of magnetic field in T
B_z_value = 0.3  # Example value for z-component of magnetic field in T
t_value = 1.0  # Example value for time in seconds

# Calculate the curl manually
curl_E = sp.Matrix([
    E_z.diff('y') - E_y.diff('z'),
    E_x.diff('z') - E_z.diff('x'),
    E_y.diff('x') - E_x.diff('y')
])

curl_B = sp.Matrix([
    B_z.diff('y') - B_y.diff('z'),
    B_x.diff('z') - B_z.diff('x'),
    B_y.diff('x') - B_x.diff('y')
])

# Define Maxwell's equations components
gauss_electricity = sp.Eq(sp.div(E_x, 'x') + sp.div(E_y, 'y') + sp.div(E_z, 'z'), rho / epsilon_0)
gauss_magnetism = sp.Eq(sp.div(B_x, 'x') + sp.div(B_y, 'y') + sp.div(B_z, 'z'), 0)
faraday = sp.Eq(curl_E, -curl_B.diff(t))
ampere_maxwell = sp.Eq(curl_B, mu_0 * sp.Matrix([J_x, J_y, J_z]) + mu_0 * epsilon_0 * curl_E.diff(t))

# Substitute the predefined values into the equations
gauss_electricity = gauss_electricity.subs({rho: rho_value})
gauss_magnetism = gauss_magnetism.subs({mu_0: mu_0})
faraday = faraday.subs({t: t_value, E_x: E_x_value, E_y: E_y_value, E_z: E_z_value, B_x: B_x_value, B_y: B_y_value, B_z: B_z_value})
ampere_maxwell = ampere_maxwell.subs({mu_0: mu_0, epsilon_0: epsilon_0, J_x: J_x_value, J_y: J_y_value, J_z: J_z_value, E_x: E_x_value, E_y: E_y_value, E_z: E_z_value, B_x: B_x_value, B_y: B_y_value, B_z: B_z_value, t: t_value})

# Display the values of the respective quantities
print("Charge Density (rho):", rho_value, "C/m^3")
print("Current Density (J_x, J_y, J_z):", J_x_value, J_y_value, J_z_value, "A/m^2")

# Print the field components
print("\nElectric Field (E_x, E_y, E_z):")
print("E_x =", E_x_value, "V/m")
print("E_y =", E_y_value, "V/m")
print("E_z =", E_z_value, "V/m")

print("\nMagnetic Field (B_x, B_y, B_z):")
print("B_x =", B_x_value, "T")
print("B_y =", B_y_value, "T")
print("B_z =", B_z_value, "T")

# Print the equations
print("\nGauss's Law for Electricity:")
sp.pprint(gauss_electricity)

print("\nGauss's Law for Magnetism:")
sp.pprint(gauss_magnetism)

print("\nFaraday's Law of Electromagnetic Induction:")
sp.pprint(faraday)

print("\n Ampere's Law with Maxwell's Addition:")
sp.pprint(ampere_maxwell)
