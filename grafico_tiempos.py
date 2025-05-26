import matplotlib.pyplot as plt

# Simula los tiempos reales obtenidos (ajústalos con tus resultados)
tiempo_original = 29.09  # Reemplaza con el tiempo real
tiempo_optimizado = 0.16  # Reemplaza con el tiempo real

# Crear la gráfica de comparación
etiquetas = ['Original', 'Optimizado']
tiempos = [tiempo_original, tiempo_optimizado]

plt.figure(figsize=(6, 4))
plt.bar(etiquetas, tiempos, color=['red', 'green'])
plt.title('Comparativa de Tiempos de Ejecución')
plt.ylabel('Tiempo (segundos)')
plt.savefig('grafico_tiempos.png')
plt.show()
