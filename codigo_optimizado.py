import time
import numpy as np
import math

def es_primo_rapido(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def buscar_primos_rapido(limite):
    numeros = np.arange(1, limite + 1)
    primos = [num for num in numeros if es_primo_rapido(num)]
    return primos

inicio = time.time()
primos = buscar_primos_rapido(100000)
fin = time.time()

print(f"Se encontraron {len(primos)} números primos.")
print(f"Tiempo de ejecución optimizado: {fin - inicio:.2f} segundos.")
