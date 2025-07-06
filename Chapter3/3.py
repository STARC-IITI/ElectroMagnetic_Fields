#Ohm's Law in Point Form:
class OhmsLaw:
    def __init__(self, voltage, resistance, current):
        self.voltage = voltage
        self.resistance = resistance
        self.current = current

    def calculate_voltage(self):
        self.voltage = self.resistance * self.current

    def calculate_current(self):
        self.current = self.voltage / self.resistance

    def calculate_resistance(self):
        self.resistance = self.voltage / self.current

# Example usage:
ohms_law = OhmsLaw(voltage=10, resistance=2, current=None)
ohms_law.calculate_current()

# Display results
print("Voltage (V):", ohms_law.voltage)
print("Current (A):", ohms_law.current)
print("Resistance (Ohms):", ohms_law.resistance)
