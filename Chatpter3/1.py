#Current and Current Density:
class Current:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction

class CurrentDensity:
    def __init__(self, current, area):
        self.current = current
        self.area = area

# Example usage:
current = Current(5, "A")
area = 2  # m^2
current_density = CurrentDensity(current, area)

# Display results
print("Current Magnitude:", current.magnitude)
print("Current Direction:", current.direction)
print("Current Density (A/m^2):", current_density.current.magnitude / current_density.area)

