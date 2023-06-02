import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Valores experimentales de energía
experimental_energy_levels = np.array([-4.35, -4.85, -5.1, -5.15, -10.2, -10.7, -10.95, -11.0, -14.9, -15.4])

# Valores de L y S
L_values = np.arange(0, 5)  # Valores de L
S_values = np.arange(0, 2)  # Valores de S

# Número de subniveles
num_sublevels = len(L_values) * len(S_values)

# Arreglos para almacenar los niveles de energía simulados y las etiquetas
energy_levels_simulated = np.zeros((num_sublevels,))
labels = []

# Función objetivo para minimizar la diferencia entre valores simulados y experimentales
def objective(params):
    A, B, scale = params
    energy_diff = []
    index = 0
    for L in L_values:
        for S in S_values:
            J_values = np.arange(np.abs(L - S), L + S + 1)
            energy = scale * (-A * L**2 - B * (S*(S+1) - L*(L+1) - J_values*(J_values+1)).mean())
            energy_levels_simulated[index] = energy
            energy_diff.append(experimental_energy_levels[index] - energy)
            error_percent = abs(energy_diff[-1] / experimental_energy_levels[index]) * 100
            print(f'Energía para L={L}, S={S}: {energy:.2f} eV, Error porcentual: {error_percent:.2f}%')
            index += 1
    return np.mean(np.abs(energy_diff))

# Realizar ajuste de parámetros utilizando el método de mínimos cuadrados
result = minimize(objective, [2.0, 1.0, 1.0])
A_opt, B_opt, scale_opt = result.x

# Calcular los niveles de energía simulados utilizando los parámetros óptimos
index = 0
for L in L_values:
    for S in S_values:
        J_values = np.arange(np.abs(L - S), L + S + 1)
        energy = scale_opt * (-A_opt * L**2 - B_opt * (S*(S+1) - L*(L+1) - J_values*(J_values+1)).mean())
        energy_levels_simulated[index] = energy
        labels.append(f'L={L}, S={S}\n{energy:.2f} eV')
        index += 1

# Calcular el error porcentual entre los valores simulados y experimentales
error_percent = np.abs((energy_levels_simulated - experimental_energy_levels) / experimental_energy_levels) * 100
mean_error_percent = np.mean(error_percent)
print(f'\nError porcentual promedio: {mean_error_percent:.2f}%')

# Graficar los niveles de energía simulados y experimentales
plt.figure(figsize=(8, 6))
plt.scatter(np.arange(num_sublevels), energy_levels_simulated, color='blue', label='Simulado')
plt.scatter(np.arange(num_sublevels), experimental_energy_levels, color='green', label='Experimental')
plt.xticks(np.arange(num_sublevels), labels, rotation='vertical')
plt.ylabel('Energía (eV)')
plt.title('Estructura Fina en el Átomo de Hidrógeno')
plt.legend()
plt.tight_layout()
plt.show()
