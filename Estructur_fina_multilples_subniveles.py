import numpy as np
import matplotlib.pyplot as plt

# Constantes de proporcionalidad
A = 1.0
B = 1.0

# Valores de L y S
L_values = np.arange(0, 5)  # Valores de L
S_values = np.arange(0, 2)  # Valores de S

# Número de subniveles
num_sublevels = len(L_values) * len(S_values)

# Arreglos para almacenar los niveles de energía y las etiquetas
energy_levels = np.zeros((num_sublevels,))
labels = []

# Calcular los niveles de energía para diferentes valores de L y S
index = 0
for L in L_values:
    for S in S_values:
        j_values = np.arange(np.abs(L - S), L + S + 1)
        energy = -A * L**2 - B * (S*(S+1) - L*(L+1) - j_values*(j_values+1)).mean()
        energy_levels[index] = energy
        labels.append(f'L={L}, S={S}\n{energy:.2f} eV')
        index += 1

# Graficar los niveles de energía
plt.figure()
plt.plot(np.arange(num_sublevels), energy_levels, 'bo')
plt.xticks(np.arange(num_sublevels), labels, rotation='vertical')
plt.xlabel('Subniveles')
plt.ylabel('Energía (eV)')
plt.title('Estructura Fina en los Niveles de Energía')
plt.tight_layout()
plt.show()

# Calcular la diferencia de energía entre niveles
energy_diff = np.diff(energy_levels)
print("Energía de cada caso:")
for i, energy in enumerate(energy_levels):
    print(f"{labels[i]}: {energy:.2f} eV")

print("\nDiferencia de energía entre niveles:")
for i, diff in enumerate(energy_diff):
    print(f"{labels[i]} - {labels[i+1]}: {diff:.2f} eV")
