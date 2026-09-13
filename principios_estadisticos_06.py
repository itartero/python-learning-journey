import math

# En una prueba de 10 km tenemos:

# Grupo A
tiempos_a = [39, 40, 41, 42, 43, 44, 45]
# Grupo B
tiempos_b = [20, 30, 40, 42, 44, 55, 65]

# Un ciclista tarda 45 minutos.

# ¿Es igual de excepcional obtener 45 minutos en el Grupo A que en el Grupo B?

# Sin calcular nada con Python, responde razonando:

# ¿Cuál es aproximadamente la media de cada grupo?
media_a = 42
media_b = 42.28

# En cuál de los dos grupos crees que 45 minutos está más lejos de lo habitual, ¿Por qué?
# Claramente en B esta más lejos de lo habitual. 

# Aunque la media y la mediana son practicamente identicas, los valores B se encuntran mucho más dispersos de la media y del valor objetivo de 45
# ¿Qué información necesitamos además de la media para poder comparar correctamente ese 45?
# Utiilizaría la desviación estándar. Tampoco estaría de más una representación grafica de los datos como un histograma

# Calcula para cada grupo:

# media
def media(tiempos):
    media = sum(tiempos) / len(tiempos)
    return media

# desviación estándar
def desviacion(tiempos):
    desv = 0
    for num in tiempos:
        desv += (media(tiempos) - num) ** 2
    desv = math.sqrt(desv / len(tiempos))
    return desv

print(f"La media del grupo A es {media(tiempos_a)}\nLa desviación estándar es {desviacion(tiempos_a)}")
print(f"La media del grupo B es {media(tiempos_b)}\nLa desviación estándar es {desviacion(tiempos_b)}")

# El z-score transforma la distancia respecto a la media en una medida relativa a la dispersión de los datos

# z-score

media_a = media(tiempos_a)
media_b = media(tiempos_b)
desv_a = desviacion(tiempos_a)
desv_b = desviacion(tiempos_b)

def zscore(tiempos, valor):
    score = (valor - media(tiempos)) / desviacion(tiempos)
    return score

print(f"El z-score de A respecto a 45 = {zscore(tiempos_a, 45)}")
print(f"El z-score de B respecto a 45 = {zscore(tiempos_b, 45)}")

# Sin Python, ¿qué significa cada uno de estos resultados?

# Caso A
# z = +1,5

# Caso B
# z = +0,2

# Los tiempos del grupo A se encuentran a 1,5 desviaciones estandar del tiempo objetivo de 45 
# Mientras, el grupo B se situa a tan solo 0.2 puntos con un z-score practicamente nulo

# Si un ciclista hubiera obtenido un z-score de −2, ¿qué significaría en lenguaje normal?
# Equivaldría a que ese ciclista se encuentra por encima del tiempo objetivo, en concreto -2 desviaciones estandar