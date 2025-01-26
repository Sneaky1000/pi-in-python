import numpy as np
import matplotlib.pyplot as plt

# Create an array of theta values in degrees
theta_degrees = np.linspace(0, 113*360, 100000)

# Convert degrees to radians
theta_radians = np.deg2rad(theta_degrees)

# Calculate z(theta) using the formula (1j is an immginary number)
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)

# Separate the real and imaginary parts of z
x = np.real(z)
y = np.imag(z)

# Create a plot with specified settings
plt.figure(figsize=(10, 10))
plt.plot(x, y, color = 'white', linewidth = 0.5)

plt.gca().set_facecolor('black')
plt.gca().set_aspect('equal')
plt.grid(False)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

# Display the plot
plt.show()
