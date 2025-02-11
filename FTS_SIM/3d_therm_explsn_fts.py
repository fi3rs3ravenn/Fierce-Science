# 3D animation of a thermonuclear explosion

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_title("Thermonuclear explosion (energy release)")


num_particles = 1000
positions = np.zeros((num_particles, 3))  
velocities = np.random.uniform(-0.05, 0.05, (num_particles, 3))


particles, = ax.plot([], [], [], 'ro', markersize=5, label="Energy release")


def update_explosion(frame):
    global positions, velocities

    positions += velocities

    particles.set_data(positions[:, 0], positions[:, 1])
    particles.set_3d_properties(positions[:, 2])

    return particles,

ani_explosion = animation.FuncAnimation(fig, update_explosion, frames=100, interval=30, blit=True)
plt.legend()
plt.show()
