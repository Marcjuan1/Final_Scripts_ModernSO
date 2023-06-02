import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros del campo magnético
B = 1.5  # Magnitud del campo magnético en Tesla
omega_L = 1.0  # Frecuencia angular del campo magnético en radianes por segundo

# Parámetros del electrón de valencia del átomo de oro
spin = 0.5  # Espín del electrón
g_factor = 2.0023  # Factor g del electrón de valencia del oro

# Variables para almacenar el cambio de spin
spin_changes = []

# Función para calcular la evolución temporal del espín
def spin_evolution(t):
    """
    Calcula la dirección del espín del electrón en función del tiempo.
    """
    theta = omega_L * t
    phi = g_factor * B * t
    spin_x = spin * np.sin(theta) * np.cos(phi)
    spin_y = spin * np.sin(theta) * np.sin(phi)
    spin_z = spin * np.cos(theta)
    return spin_x, spin_y, spin_z

# Función para calcular la trayectoria del electrón
def electron_trajectory(t):
    """
    Calcula la trayectoria del electrón en función del tiempo.
    """
    r = 0.5  # Radio de la trayectoria circular
    omega = omega_L  # Frecuencia angular de la trayectoria circular
    x = r * np.cos(omega * t)
    y = r * np.sin(omega * t)
    z = 0.0  # La trayectoria es en el plano XY
    return x, y, z

# Función para calcular el vector de flujo magnético en el electrón
def magnetic_flux(t):
    """
    Calcula el vector de flujo magnético en el electrón en función del tiempo.
    """
    x, y, z = electron_trajectory(t)
    flux_x = -B * y
    flux_y = B * x
    flux_z = 0.0
    return flux_x, flux_y, flux_z

# Crear figura y ejes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.6, 0.6)
ax.set_zlim(-0.6, 0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Variables para almacenar la trayectoria, el espín y el flujo magnético en cada tiempo
trajectory = []
spin_values = []
flux_values = []

# Función de actualización para la animación
def update(frame):
    ax.cla()  # Limpiar los ejes antes de cada actualización
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_zlim(-0.6, 0.6)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Tiempo = {frame} s')

    # Calcular la dirección del espín en el tiempo actual
    spin_x, spin_y, spin_z = spin_evolution(frame)

    # Calcular la trayectoria del electrón en el tiempo actual
    x, y, z = electron_trajectory(frame)
    trajectory.append((x, y, z))
    spin_values.append((spin_x, spin_y, spin_z))

    # Calcular el vector de flujo magnético en el tiempo actual
    flux_x, flux_y, flux_z = magnetic_flux(frame)
    flux_values.append((flux_x, flux_y, flux_z))

    # Graficar la trayectoria del electrón
    trajectory_array = np.array(trajectory)
    ax.plot(trajectory_array[:, 0], trajectory_array[:, 1], trajectory_array[:, 2], 'r--')

    # Graficar el electrón como un punto en la trayectoria
    ax.scatter(x, y, z, color='b')

    # Graficar el espín como un vector en el punto actual
    ax.quiver(x, y, z, spin_x, spin_y, spin_z, length=0.2, normalize=True, color='g')

    # Mostrar el valor de spin en la animación
    ax.text(x, y, z + 0.1, f'Spin = ({spin_x:.2f}, {spin_y:.2f}, {spin_z:.2f})')

    # Graficar el vector de flujo magnético en el plano XY
    ax.quiver(x, y, z, flux_x, flux_y, flux_z, length=0.1, normalize=True, color='m')

    # Calcular el cambio de spin promedio
    if len(spin_values) > 1:
        spin_change = np.array(spin_values[-1]) - np.array(spin_values[-2])
        spin_changes.append(np.linalg.norm(spin_change))

# Crear la animación
animation = FuncAnimation(fig, update, frames=np.linspace(0, 10, 200), interval=50)

# Mostrar la animación
plt.show()

# Calcular el cambio de spin promedio
average_spin_change = np.mean(spin_changes)
print(f'Cambio de spin promedio: {average_spin_change}')
