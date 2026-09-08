import math

# 1. El problema

# Imagina dos ciclistas que han tardado, en minutos, en completar 7 recorridos:

# Ciclista A
tiempos_a = [48, 49, 50, 51, 52, 49, 51]

# Ciclista B
tiempos_b = [30, 35, 40, 50, 60, 65, 70]

# Antes de calcular nada, piensa.

# Pregunta 1

# Calcula mentalmente o con Python:

# Media de A
# Media de B

# ¿Son muy diferentes?

# Media Ciclista A = 50
# Media Ciclista B = 50

# Pregunta 2

# Ahora observa los datos.

# ¿Cuál de los dos ciclistas parece tener un rendimiento más regular?
# Ciclista A

# ¿Y cuál parece tener un rendimiento más variable?
# Ciclista B

# Calcula el rango de:

tiempos_a = [48, 49, 50, 51, 52, 49, 51]
tiempos_b = [30, 35, 40, 50, 60, 65, 70]

# rango_b = 70 - 30 = 40
# rango_a = 52 - 48 = 4 

# Y responde:

# ¿Qué nos está diciendo el rango de cada ciclista?

# Ciclista B maneaja muchos más valores que el ciclista A

# En Python, crea un pequeño script o notebook y trabaja con los dos conjuntos:

tiempos_a = [48, 49, 50, 51, 52, 49, 51]
tiempos_b = [30, 35, 40, 50, 60, 65, 70]

# Calcula para cada uno: Media, Mínimo, Máximo, Rango
media_a = sum(tiempos_a) / len(tiempos_a)
media_b = sum(tiempos_b) / len(tiempos_b)
min_a = min(tiempos_a)
min_b = min(tiempos_b)
max_a = max(tiempos_a)
max_b = max(tiempos_b)
rango_a = max_a - min_a
rango_b = max_b - min_b

# Después intenta averiguar cómo calcular:
# Varianza
# Desviación estándar
# Puedes investigar cómo hacerlo con Python/NumPy.

tiempos_a = [48, 49, 50, 51, 52, 49, 51]
tiempos_b = [30, 35, 40, 50, 60, 65, 70]

def varianza_a(tiempos_a):
    sum_var = 0
    var_a = 0
    for num in tiempos_a:
        sum_var += (num - media_a) ** 2
    var_a = sum_var / len(tiempos_a)
    return var_a

def varianza_b(tiempos_b):
    sum_var = 0
    var_b = 0
    for num in tiempos_b:
        sum_var += (num - media_b) ** 2
    var_b = sum_var / len(tiempos_b)
    return var_b

desv_a = math.sqrt(varianza_a(tiempos_a))
desv_b = math.sqrt(varianza_b(tiempos_b))

print(f"Datos Ciclista A\nMedia = {media_a}\nMínimo = {min_a}\nMáximo = {max_a}\nRango = {rango_a}\nVarianza = {varianza_a(tiempos_a)}\nDesviación Estándar = {desv_a}\n")
print(f"Datos Ciclista B\nMedia = {media_b}\nMínimo = {min_b}\nMáximo = {max_b}\nRango = {rango_b}\nVarianza = {varianza_b(tiempos_b)}\nDesviación Estándar = {desv_b}")
        
# Cuando termines, quiero que seas capaz de responder con tus propias palabras:

# 1. ¿Qué mide el rango?
# rango = "La diferencia entre el valor máximpo y mínimo de un conjunto de datos. Es una primera medida de cuan distantes pueden estar los datos de una muestra"

# 2. ¿Qué significa que un conjunto tenga una desviación estándar pequeña?
# La dispersión de sus datos es baja. No se distancian mucho los valores de su media

# 3. Si dos conjuntos tienen exactamente la misma media, ¿pueden tener desviaciones estándar muy diferentes? ¿Por qué?
# Perfectamente. Los datos pueden sumar la misma cifra y ser valores completamente diferentes