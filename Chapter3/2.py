#Continuity of Current:
class ContinuityEquation:
    def __init__(self, in_current, out_current, rate_of_change):
        self.in_current = in_current
        self.out_current = out_current
        self.rate_of_change = rate_of_change

    def verify_continuity(self):
        return self.in_current - self.out_current == self.rate_of_change

# Example usage:
continuity_eq = ContinuityEquation(in_current=10, out_current=6, rate_of_change=4)

# Display result
is_continuity_maintained = continuity_eq.verify_continuity()
print("Is Continuity Maintained?", is_continuity_maintained)
