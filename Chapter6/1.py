# Faraday's law
initial_flux = 0.0  # Initial magnetic flux (in Weber, Wb)
final_flux = 0.2  # Final magnetic flux (in Weber, Wb)
time_interval = 2.0  # Time interval (in seconds)

# Calculate the rate of change of magnetic flux (dphi/dt)
dPhi_dt = (final_flux - initial_flux) / time_interval

# Calculate the induced electromotive force (EMF) using Faraday's law
EMF = -dPhi_dt

# Display the details
print("Initial Magnetic Flux (phi_initial):", initial_flux, "Wb")
print("Final Magnetic Flux (phi_final):", final_flux, "Wb")
print("Time Interval (delta_t):", time_interval, "s")
print("Rate of Change of Magnetic Flux (dphi/dt):", dPhi_dt, "Wb/s")
print("Induced Electromotive Force (EMF):", EMF, "V")
