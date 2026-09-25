import numpy as np

# Fijamos semilla para que el experimento sea reproducible
np.random.seed(42)

# Generamos 10.000 datos que siguen una distribución normal perfecta
mu = 1200     # Media: el centro
sigma = 20    # Desviación estándar: el tamaño del salto

pesos = np.random.normal(loc=mu, scale=sigma, size=10000)

# Contamos cuántos caen dentro de 1 salto (μ - 1σ  y  μ + 1σ)
dentro_1_sigma = [p for p in pesos if (mu - sigma) <= p <= (mu + sigma)]
porcentaje_1_sigma = (len(dentro_1_sigma) / len(pesos)) * 100

# Contamos cuántos caen dentro de 2 saltos (μ - 2σ  y  μ + 2σ)
dentro_2_sigma = [p for p in pesos if (mu - 2*sigma) <= p <= (mu + 2*sigma)]
porcentaje_2_sigma = (len(dentro_2_sigma) / len(pesos)) * 100

print(f"Porcentaje dentro de 1σ (1180g a 1220g): {porcentaje_1_sigma:.2f}%")
print(f"Porcentaje dentro de 2σ (1160g a 1240g): {porcentaje_2_sigma:.2f}%")

cuadro_ejemplo = 1240

z_1240 = (cuadro_ejemplo - mu) / sigma

print(f"El valor 1240 se encuentra a {z_1240:.2f} desviaciones estándar de la media")

# Contamos cuántos cuadros pesan más de 1240 g (z > +2)
cola_derecha = [p for p in pesos if p > (mu + 2 * sigma)]
porcentaje_cola_derecha = (len(cola_derecha) / len(pesos)) * 100

print(f"Porcentaje simulado con peso > 1240g: {porcentaje_cola_derecha:.2f}%")

# Si el control de calidad de la fábrica rechaza automáticamente cualquier cuadro que pese más de 1240g por considerarlo fuera de especificación:
# ¿Qué porcentaje de la producción se descartará por exceso de peso? 
# Si la fábrica produce 10.000 cuadros al mes, ¿cuántos cuadros defectuosos por sobrepeso se espera descartar aproximadamente?

rechazados = (2.5 * 10000) / 100
print(f"Rechazará aproximadamente unos {rechazados} cuadros")

from scipy import stats

# Parámetros del proceso
mu = 1200       # Media (mu)
sigma = 20      # Desviación estándar (sigma)
limite = 1235   # Límite superior de tolerancia

# Probabilidad acumulada por debajo de 1235 g
p_menor = stats.norm.cdf(limite, loc=mu, scale=sigma)

# Probabilidad por encima de 1235 g (rechazo)
p_mayor = 1 - p_menor

print(f"Porcentaje dentro de tolerancia (<= 1235g): {p_menor * 100:.2f}%")
print(f"Porcentaje de rechazo (> 1235g): {p_mayor * 100:.2f}%")

# Escribe un bloque de código en tu script que:
# Calcule con stats.norm.ppf() el peso límite exacto que deja por debajo al 99% de la producción ($0.99$)
nuevo_limite = stats.norm.ppf(0.99, loc = 1200, scale = 20)

# Calcule el Z-score correspondiente a ese nuevo peso límite:
z_1153 = (nuevo_limite - 1200) / 20

# Imprima ambos valores por consola formateados a dos decimales.

print(f"El nuevo límite superior es: {nuevo_limite:.2f}")
print(f"Se situa a {z_1153:.2f} desviaciones estándar")

# ¿Qué peso máximo debe tolerar la fábrica para no superar ese 1% de rechazos?
# 1246.53 gramos