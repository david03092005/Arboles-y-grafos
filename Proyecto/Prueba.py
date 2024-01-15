import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# # Datos de ejemplo (matriz de interacciones entre nodos)
# interacciones = np.array([
#     [20, 10, 5, 2],
#     [8, 15, 3, 1],
#     [5, 2, 18, 12],
#     [2, 1, 10, 25]
# ])

# # Etiquetas para los nodos
# nodos = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D']

# # Crear un mapa de calor
# sns.heatmap(interacciones, annot=True, fmt='d', cmap='coolwarm', xticklabels=nodos, yticklabels=nodos)

# # Agregar etiquetas y título al gráfico
# plt.xlabel('Nodos')
# plt.ylabel('Nodos')
# plt.title('Mapa de Calor de Interacciones')

# # Mostrar el gráfico
# plt.show()


# # Datos de ejemplo (distribución de opiniones en una red social)
# grupos = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F']
# opiniones = [0.8, -0.5, 0.2, -0.7, 0.9, 0.1]

# # Crear un diagrama de polarización
# # plt.figure(figsize=(8, 6))
# plt.polar(np.linspace(0, 2 * np.pi, len(grupos), endpoint=False), opiniones, marker='o', linestyle='-')

# # Personalizar el gráfico
# plt.thetagrids(range(0, 360, int(360/len(grupos))), labels=grupos)
# plt.title('Diagrama de Polarización en Redes Sociales')

# # Mostrar el gráfico
# plt.show()



# # Definir parámetros
# h = 5
# pi = np.pi
# i_values = np.arange(0, h, 1)
# j_values = np.arange(0, h, 1)

# # Crear una cuadrícula para i y j
# i, j = np.meshgrid(i_values, j_values)

# # Calcular la ponderación según la fórmula dada
# weight = pi**(2.6*i) * pi**j

# # Crear un gráfico tridimensional
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(i, j, weight, cmap='viridis')

# # Etiquetas y título
# ax.set_xlabel('i')
# ax.set_ylabel('j')
# ax.set_zlabel('Ponderación')
# ax.set_title('Ponderación de Polarización en función de i y j')

# plt.show()


# # Datos de ejemplo: tiempo en meses y opiniones de tres personas
# tiempo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# persona1 = np.array([3, 4, 4, 3, 2, 1, 1, 2, 3, 4])
# persona2 = np.array([5, 4, 4, 3, 3, 3, 2, 2, 1, 1])
# persona3 = np.array([1, 2, 3, 4, 4, 3, 3, 4, 5, 5])

# # Graficar las opiniones de cada persona a lo largo del tiempo
# plt.plot(tiempo, persona1, label='Persona 1', marker='o')
# plt.plot(tiempo, persona2, label='Persona 2', marker='o')
# plt.plot(tiempo, persona3, label='Persona 3', marker='o')

# # Personalizar el gráfico
# plt.title('Polarización de Opiniones a lo largo del Tiempo')
# plt.xlabel('Tiempo (meses)')
# plt.ylabel('Opiniones')
# plt.legend()  # Agregar leyenda

# # Mostrar el gráfico
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
cantidadNodos = 8
nodos = np.arange(cantidadNodos)
polarizacion = np.random.uniform(0, 1, size=cantidadNodos)
tamanio_burbujas = polarizacion * 1000  # Ajusta el rango según tus datos

# Crear el gráfico de burbujas
plt.scatter(nodos, nodos, s=tamanio_burbujas, c=polarizacion, cmap='coolwarm', alpha=0.7)

# Personalizar el gráfico
plt.title('Gráfico de Burbujas de Polarización en Redes Sociales')
plt.xlabel('Nodos')
plt.ylabel('Nodos')
plt.colorbar(label='Polarización')

plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
cantidadNodos = 8
nodos = np.arange(cantidadNodos)
conexiones = np.random.randint(0, 2, size=(cantidadNodos, cantidadNodos))

# Crear el gráfico de red desde cero
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Posiciones de los nodos
posiciones = np.random.rand(cantidadNodos, 2)

# Dibujar nodos
for i, (x, y) in enumerate(posiciones):
    ax.scatter(x, y, color='skyblue', s=200, edgecolors='black', linewidths=2, zorder=2)
    ax.text(x, y, str(i), color='black', ha='center', va='center', fontsize=10, fontweight='bold', zorder=3)

# Dibujar conexiones entre nodos
for i in range(cantidadNodos):
    for j in range(i + 1, cantidadNodos):
        if conexiones[i, j] == 1:
            ax.plot([posiciones[i, 0], posiciones[j, 0]], [posiciones[i, 1], posiciones[j, 1]], color='gray', linewidth=1, zorder=1)

# Personalizar el gráfico
ax.set_title('Gráfico de Red de Polarización en Redes Sociales')

# Mostrar el gráfico
plt.show()