import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

num_particles = 10  
box_size = 1.2  
collision_distance = 0.15

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-box_size, box_size)
ax.set_ylim(-box_size, box_size)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Animation of thermonuclear fusion")

particles, = ax.plot([], [], 'ro', markersize=10, label="Hydrogen nuclei")
fusion, = ax.plot([], [], 'yo', markersize=20, label="Synthesis reaction", alpha=0)  
energy_wave, = ax.plot([], [], 'bo', markersize=5, alpha=0, label="Energy released")  

positions = np.random.uniform(-box_size, box_size, (num_particles, 2))
velocities = np.random.uniform(-0.02, 0.02, (num_particles, 2))

def update(frame):
    global positions, velocities

    positions += velocities

    for i in range(num_particles):
        for j in range(2):  
            if abs(positions[i, j]) > box_size:
                velocities[i, j] *= -1  

    reaction_triggered = False
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            distance = np.linalg.norm(positions[i] - positions[j])
            if distance < collision_distance:  
                fusion.set_data([(positions[i, 0] + positions[j, 0]) / 2], 
                                [(positions[i, 1] + positions[j, 1]) / 2])
                fusion.set_alpha(1)  
                

                energy_wave.set_data(np.random.uniform(-box_size, box_size, 10),
                                     np.random.uniform(-box_size, box_size, 10))
                energy_wave.set_alpha(0.5)
                
                reaction_triggered = True
                break 

    if not reaction_triggered:
        fusion.set_alpha(0)  
        energy_wave.set_alpha(0)  


    particles.set_data(positions[:, 0], positions[:, 1])
    
    return particles, fusion, energy_wave


ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)
plt.legend()
plt.show()
