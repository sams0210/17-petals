import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the flower parameters
num_petals = 17
theta = np.linspace(0, 2 * np.pi, 300)

# Function to create petal shape
def petal_shape(a):
    r = 1 + a * np.sin(num_petals * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Initialize the plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Initialize the petals
petals, = ax.plot([], [], lw=2)

# Update function for animation
def update(frame):
    a = frame / 100  # Animation progress
    x, y = petal_shape(a)
    petals.set_data(x, y)
    return petals,

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
