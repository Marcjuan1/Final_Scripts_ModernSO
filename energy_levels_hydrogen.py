import numpy as np
import matplotlib.pyplot as plt

def energy_level(n, l):
    """
    Calcula la energía del nivel n y momento angular orbital l para el átomo de hidrógeno
    """
    return -13.6 / (n**2)  # Energía sin considerar la interacción Spín-órbita

def energy_level_spin_orbit(n, l):
    """
    Calcula la energía del nivel n y momento angular orbital l considerando la interacción Spín-órbita
    """
    return energy_level(n, l) - (1/2) * (l * (l + 1) - 3/4) / (n**2)

n_values = [1, 2, 3]  # Valores de n para los niveles de energía
l_values = [0, 1, 2]  # Valores de l para los niveles de energía

# Energías sin considerar la interacción Spín-órbita
energies = [[energy_level(n, l) for l in l_values] for n in n_values]

# Energías considerando la interacción Spín-órbita
energies_spin_orbit = [[energy_level_spin_orbit(n, l) for l in l_values] for n in n_values]

# Graficar los niveles de energía antes y después de la inclusión de la interacción Spín-órbita
plt.figure(figsize=(8, 6))
for i in range(len(n_values)):
    plt.plot(l_values, energies[i], 'o-', label=f'n={n_values[i]} (sin Spín-órbita)')
    plt.plot(l_values, energies_spin_orbit[i], 'o-', label=f'n={n_values[i]} (con Spín-órbita)')
    print(f"Niveles de energía para n={n_values[i]}:")
    print(f"Sin Spín-órbita: {energies[i]}")
    print(f"Con Spín-órbita: {energies_spin_orbit[i]}\n")
plt.xlabel('l (momento angular orbital)')
plt.ylabel('Energía (eV)')
plt.title('Niveles de Energía del Átomo de Hidrógeno')
plt.legend()
plt.grid(True)
plt.show()
