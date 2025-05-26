import pstats
import matplotlib.pyplot as plt

# Cargar archivo generado con cProfile
stats = pstats.Stats('profiling_optimizado.txt')
stats.strip_dirs().sort_stats('cumtime')

# Obtener las 10 funciones que más tiempo consumen
funciones = []
tiempos = []

for func, stat in list(stats.stats.items())[:10]:
    nombre_funcion = f"{func[2]} ({func[0].split('/')[-1]}:{func[1]})"
    funciones.append(nombre_funcion)
    tiempos.append(stat[3])  # tiempo total acumulado (cumulative time)

# Graficar
plt.figure(figsize=(10, 6))
plt.barh(funciones, tiempos, color='steelblue')
plt.xlabel("Tiempo acumulado (segundos)")
plt.title("Distribución de tiempos de ejecución por función (Top 10)")
plt.gca().invert_yaxis()  # Función más lenta arriba
plt.tight_layout()
plt.savefig("distribucion_tiempos.png")
plt.show()
