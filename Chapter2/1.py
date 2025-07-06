#coulomb_force_calculator

def calculate_coulomb_force(q1, q2, r):
    # Elementary charge (C)
    elementary_charge = 1.60217663e-19

    # Calculate the Coulomb force
    force = (9e9) * abs((q1 * elementary_charge) * (q2 * elementary_charge)) / (r ** 2)

    return force

# Input charges and distance in terms of elementary charges
q1 = float(input("Enter the magnitude of the first charge (in elementary charges): "))
q2 = float(input("Enter the magnitude of the second charge (in elementary charges): "))
r = float(input("Enter the distance between the charges (in meters): "))

# Calculate and print the Coulomb force
coulomb_force = calculate_coulomb_force(q1, q2, r)
print(f"The Coulomb force between the charges is {coulomb_force:.2e} Newtons.")
