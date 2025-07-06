#electric field
def calculate_electric_field(q, r):
    # Coulomb's constant (N*m^2/C^2)
    k = 8.988e9

    # Calculate the electric field
    electric_field = k * abs(q) / (r ** 2)

    return electric_field

# Input charge and distance
q = float(input("Enter the magnitude of the point charge (in C): "))
r = float(input("Enter the distance from the charge (in meters): "))

# Calculate and print the electric field
electric_field = calculate_electric_field(q, r)
print(f"The electric field at the specified point is {electric_field:.2f} N/C.")
