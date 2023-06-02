import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros iniciales
radius = 1.0  # Radio de la órbita
num_points = 1000  # Número de puntos en la órbita
duration = 10  # Duración de la animación en segundos
spin_orbit_strength = 0.1  # Fuerza de interacción spin-órbita

# Coordenadas polares para la órbita
theta = np.linspace(0, 2*np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Inicialización de la figura y el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configuración de los ejes
ax.set_xlim3d([-radius, radius])
ax.set_ylim3d([-radius, radius])
ax.set_zlim3d([-radius, radius])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Dibujar núcleo en el centro de la órbita
ax.plot([0], [0], [0], 'ko', label='Núcleo')

# Inicialización de los objetos gráficos
orbit, = ax.plot(x, y, np.zeros_like(x), 'g', label='Órbita')
electron, = ax.plot([x[0]], [y[0]], [0], 'yo', label='Electrón')
spin_arrow, = ax.plot([x[0]], [y[0]], [0], 'b', label='Spin')
angular_momentum_arrow, = ax.plot([x[0]], [y[0]], [0], 'r', label='Momento Angular')

# Función de actualización de la animación
def update(frame):
    # Actualización de la posición del electrón
    electron.set_data([x[frame]], [y[frame]])
    electron.set_3d_properties([0])

    # Actualización de la posición del spin
    spin_angle = frame * 2 * np.pi / num_points
    spin_arrow.set_data([x[frame], x[frame] + np.cos(spin_angle)],
                        [y[frame], y[frame] + np.sin(spin_angle)])
    spin_arrow.set_3d_properties([0, 0])

    # Actualización de la posición del momento angular
    angular_momentum_angle = frame * 4 * np.pi / num_points
    angular_momentum_arrow.set_data([x[frame], x[frame] + np.cos(angular_momentum_angle)],
                                    [y[frame], y[frame] + np.sin(angular_momentum_angle)])
    angular_momentum_arrow.set_3d_properties([0, 0])

    # Actualización de la órbita
    orbit_radius = radius * (1 + spin_orbit_strength * np.cos(spin_angle))
    orbit.set_data(orbit_radius * np.cos(theta), orbit_radius * np.sin(theta))
    orbit.set_3d_properties(np.zeros_like(x))

    return electron, spin_arrow, angular_momentum_arrow, orbit

# Creación de la animación
ani = FuncAnimation(fig, update, frames=num_points, interval=(duration * 1000) / num_points,
                    repeat=True, blit=True)

# Mostrar leyenda y título
ax.legend()
plt.title('Interacción Spin-Órbita')

# Mostrar la animación
plt.show()
