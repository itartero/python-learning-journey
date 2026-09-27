# Vamos a volver al mundo de las bicicletas, pero con un problema diferente.

# Una tienda ha registrado cuánto tiempo tardaron 30 reparaciones:
# import panda as pd
import math
tiempos = [
    22, 35, 41, 38, 45,
    52, 47, 43, 39, 44,
    51, 48, 42, 46, 40,
    37, 49, 53, 45, 41,
    44, 47, 50, 43, 46,
    39, 55, 42, 48, 91
]

# Hay algo interesante aquí. 👀

# Pero no voy a decirte qué es.

# 🎯 Parte 1 — Investiga los datos

# En VS Code, crea un pequeño script para trabajar con esta lista.

# Primero quiero que respondas sin utilizar todavía un histograma:

tiempos = sorted(tiempos)

# Cuál es la:

# media
media = sum(tiempos) / len(tiempos)
# mediana
if len(tiempos) % 2 == 0: 
    mediana = (tiempos[int(len(tiempos) / 2)] + tiempos[int((len(tiempos) / 2) - 1)]) / 2
else:
    mediana = tiempos[int(((len(tiempos)) - 1) / 2)]
# desviación estándar
# desviacion = pd.desv(tiempos)
desviacion = 0
for num in tiempos: 
    desviacion += (num - media) ** 2
desviacion = math.sqrt(desviacion / len(tiempos))
# mínimo
minimo = min(tiempos)
# máximo
maximo = max(tiempos)

print("Media = ", media)
print("Mediana = ", mediana)
print("Desviación Estándar = ", desviacion)
print("Mínimo = ", minimo)
print("Máximo =", maximo)

# Después quiero que mires los resultados y respondas:

# ¿Crees que la media representa bien el tiempo habitual de una reparación? ¿Por qué?

# No, existen valores muy dispares con la media tanto por arriba como por abajo.

# Y la pregunta nueva

# Mira únicamente la lista de valores.

# ¿Cómo describirías la distribución de estos tiempos?

# Existen ciertos datos dispersos de la media como es 22 y 91. La desviación estandar y el rango son valores altos

# Quiero que agrupemos los tiempos en intervalos de 10 minutos:

#Sin utilizar todavía ninguna función nueva de Python:

# ¿Cuántas reparaciones caen en cada intervalo?

# 20–29 - 1
# 30–39 - 5
# 40–49 - 18
# 50–59 - 5
# 60–69 - 0
# 70–79 - 0 
# 80–89 - 0
# 90–99 - 1

# Necesitamos crear estas ocho frecuencias en Python:

# Podemos recorrer los datos con:

# for tiempo in tiempos:

# Y necesitamos averiguar:

# ¿En qué intervalo cae cada tiempo?

# Por ejemplo, para saber si un tiempo está entre 40 y 49 podríamos preguntar:

# if tiempo >= 40 and tiempo <= 49:

# Pero no quiero que escribas ocho if independientes.

# Quiero que intentes encontrar una forma de contar los valores de cada intervalo.

# Pista pequeña

# Piensa en crear algo así:

frecuencias = [0, 0, 0, 0, 0, 0, 0, 0]

# y después ir aumentando el contador correspondiente.

# Inténtalo tú.

print(tiempos)

for num in tiempos:
    if num >= 90:
        frecuencias[7] += 1
    elif num < 90 and num >= 80:
        frecuencias[6] += 1
    elif num < 80 and num >= 70:
        frecuencias[5] += 1
    elif num < 70 and num >= 60:
        frecuencias[4] += 1
    elif num < 60 and num >= 50:
        frecuencias[3] += 1
    elif num < 50 and num >= 40:
        frecuencias[2] += 1
    elif num < 40 and num >= 30:
        frecuencias[1] += 1
    else:
        frecuencias[0] += 1

print(frecuencias)

intervalos = ["20-29", "30-39", "40-49", "50-59",
              "60-69", "70-79", "80-89", "90-99"]

import matplotlib.pyplot as plt

plt.hist(tiempos, bins = 18)

plt.savefig("distribucion_tiempos.png")

# Si fueras el responsable del taller y tuvieras que resumir estos 30 tiempos de reparación a alguien que pregunta "¿cuánto suele tardar una reparación?", ¿qué responderías?

# Le respondería que la media es en unos 45 minutos aprox. pero que en ocasiones alguna reparacion puede distar de ese tiempo por diversas razones
# En cualquier caso, en el tiempo medido, nos movemos entre los 22 y los 91 minutos
# Con una desviación estándar de 10.5 minutos podemos decir que en el contexto de estos valores, los resultados tienen una distribución dispersa
# Esto probablemente se deba a que la pericia del mecanico, los repuestos necesarios y la naturaleza de la reparación no siempre es la misma