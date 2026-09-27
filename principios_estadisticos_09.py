import numpy as np
import matplotlib.pyplot as plt
import math

# Fijamos semilla para reproducibilidad
np.random.seed(42)

# Población de 50.000 llamadas con fuerte asimetría positiva
# (media real alrededor de 5 minutos)
poblacion = np.random.exponential(scale=5.0, size=50000)

# Calcular e imprimir por consola la media y la desviación estándar de poblacion usando np.mean() y np.std().
# Generar el histograma con plt.hist(poblacion, bins=50) y lanzarlo con plt.show().   
# Decirme qué valores te salieron y cómo describirías la forma de esa gráfica (¿es simétrica o tiene asimetría/sesgo?).

# Alternativa a np.mean(poblacion)
mu = sum(poblacion) / len(poblacion)

# Alternativa a np.std(poblacion)
sigma = 0
for data in poblacion:
    sigma += (data - mu) ** 2
sigma = math.sqrt(sigma / len(poblacion))

print(f"Media = {mu:.2f}")
print(f"Desviación Estandar = {sigma:.2f}")

plt.hist(poblacion, bins = 50)
plt.show()

# No tiene ninguna simetria, es asimetrica positiva derecha 

# Crea una lista vacía llamada medias_muestrales = [].
medias_muestrales = []

# Escribe un bucle que se repita 1.000 veces.
count = 0
while count < 1001:
# En cada iteración:
# Extrae una muestra de tamaño 30 usando np.random.choice(poblacion, size=30).
# Calcula la media de esa muestra (np.mean(...)).
# Guarda esa media en la lista medias_muestrales.
    muestra = np.random.choice(poblacion, size = 30)
    medias_muestrales.append(np.mean(muestra))
    count += 1

# Dibuja el histograma de medias_muestrales con plt.hist(medias_muestrales, bins=30) y muéstralo con plt.show().
plt.hist(medias_muestrales, bins = 50)
plt.show()

# Comprobación empírica del Teorema Central del Límite
media_de_medias = np.mean(medias_muestrales)
se_simulado = np.std(medias_muestrales)
se_teorico = sigma / np.sqrt(30)

print(f"Media de la población original (μ): {mu:.2f}")
print(f"Media de las 1.000 muestras:        {media_de_medias:.2f}")
print("---")
print(f"Error Estándar simulado (std de medias): {se_simulado:.2f}")
print(f"Error Estándar teórico (σ / √30):        {se_teorico:.2f}")

se_teorico_100 = sigma / np.sqrt(100)
print(f"Error Estándar teórico (σ / √100):        {se_teorico_100:.2f}")