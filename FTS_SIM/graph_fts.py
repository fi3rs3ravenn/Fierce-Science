import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ace_tools as tools

labels = ['Sun Core Temperature', 'Atomic Reactor Temperature', 'Coal Burning Temperature', 'Fusion Temperature']
temperatures = [15000000, 3000, 1000, 150000000] 

plt.figure(figsize=(10,6))
plt.barh(labels, temperatures, color=['orange', 'blue', 'gray', 'red'])
plt.xlabel('Temperature (°C)')
plt.title('Comparison of temperatures of different processes')
plt.xscale('log') 
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

years = np.arange(2000, 2026, 5)
costs = [5, 7, 10, 13, 17, 22] 

plt.figure(figsize=(10,6))
plt.plot(years, costs, marker='o', linestyle='-', color='green')
plt.xlabel('Year')
plt.ylabel('Investments ($ billion)')
plt.title('Increase in funding for the ITER project')
plt.grid(True)
plt.show()


sources = ['1 liter of sea water', '1 kg of oil', '1 kg of coal']
energy = [300000, 40, 24]

plt.figure(figsize=(10,6))
plt.bar(sources, energy, color=['blue', 'black', 'gray'])
plt.xlabel('Energy source')
plt.ylabel('Energy output (MJ)')
plt.title('Comparison of energy intensity of different sources')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
