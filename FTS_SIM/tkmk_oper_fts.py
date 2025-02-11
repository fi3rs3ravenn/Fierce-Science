# Visualization of the operation of a tokamak (magnetic plasma confinement)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Magnetic plasma confinement in a tokamak")

plasma, = ax.plot([], [], 'ro', markersize=20, alpha=0.6, label="Plasma")

theta = np.linspace(0, 2 * np.pi, 100)
radii = np.linspace(0.3, 1.1, 5)
field_lines = [ax.plot(np.cos(theta) * r, np.sin(theta) * r, 'b', alpha=0.3)[0] for r in radii]

def update_tokamak(frame):

    plasma.set_data([0], [0])  
    plasma.set_markersize(20 + 5 * np.sin(frame / 10))  

    for i, line in enumerate(field_lines):
        r = radii[i] + 0.02 * np.sin(frame / 5 + i) 
        line.set_data(np.cos(theta) * r, np.sin(theta) * r)

    return [plasma] + field_lines


ani_tokamak = animation.FuncAnimation(fig, update_tokamak, frames=100, interval=50, blit=True)
plt.legend()
plt.show()
