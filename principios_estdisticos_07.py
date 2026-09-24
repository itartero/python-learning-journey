import math

# Vamos a trabajar con un caso práctico sobre los tiempos de entrega (en minutos) de un servicio de mensajería en bicicleta 🚴.

# Aquí tienes los 10 tiempos registrados (ya ordenados de menor a mayor):

tiempos = [12, 14, 15, 15, 16, 18, 20, 22, 45, 50]

# 🧩 Ejercicio 1: Comparación de medidas centrales

# Para empezar a analizar la forma de la distribución:

# Obtén la media 🧮 y la mediana 📍 de este conjunto de datos (puedes calcularlas a mano o escribir una función sencilla en Python).

def media(tiempos):
    media_t = sum(tiempos) / len(tiempos)
    return media_t

def mediana(tiempos):
    tiempos = sorted(tiempos)
    if len(tiempos) % 2 == 0:
        mediana_t = ((tiempos[(len(tiempos) // 2) - 1]) + (tiempos[len(tiempos) // 2])) / 2
    else:
        mediana_t = tiempos[len(tiempos) // 2]
    return mediana_t


print("Media = ", media(tiempos))
print("Mediana = ", mediana(tiempos))

#¿Qué relación observas entre ambos valores (cuál es mayor y por cuánto difieren aproximadamente)?

# La media es mayor que la mediana en 5.7 minutos. Esto ya nos esta diciendo que nos vamos a encontrar algún dato atípico por encima de la media

# 🧩 Ejercicio 2: El dilema de la medida de dispersión

# En la Sesión 3 trabajamos con la desviación estándar, la cual utiliza la media para medir cuánto varían los datos.

# Sabiendo que en este caso la media está distorsionada por los entregas de 45 y 50 minutos:

# ¿Crees que la desviación estándar es la mejor medida para describir la dispersión habitual de este grupo, o nos daría una falsa sensación de que todos los tiempos varían mucho?

def desv(tiempos):
    desv_t = 0
    for t in tiempos:
        desv_t += (t - media(tiempos)) ** 2
    desv_t = math.sqrt(desv_t / len(tiempos))
    return desv_t

print(f"Desviación Estándar = {desv(tiempos)}")

# ¿Qué alternativa podríamos usar?

# Se puede utilizar una representación gráfica como un histograma

# 🧩 Ejercicio 3: Cálculo de Cuartiles e IQR

# Tenemos nuestros 10 tiempos ordenados:

tiempos = [12, 14, 15, 15, 16, 18, 20, 22, 45, 50]

# Si dividimos la lista en dos mitades usando la mediana: 

tiempos_q2 = 17

tiempos_sub1 =  [12, 14, 15, 15, 16]
tiempos_sub2 =  [18, 20, 22, 45, 50]

# ¿Cuál es el valor central ($Q_1$) de la primera mitad?

tiempos_q1 = mediana(tiempos_sub1)

print(f"Q1 = {tiempos_q1}")

# ¿Cuál es el valor central ($Q_3$) de la segunda mitad?

tiempos_q3 = mediana(tiempos_sub2)

print(f"Q3 = {tiempos_q3}")

# Sabiendo $Q_1$ y $Q_3$, ¿cuánto vale el IQR ($Q_3 - Q_1$)?

def iqr(tiempos):
    tiempos_iqr = tiempos_q3 - tiempos_q1
    return tiempos_iqr

print(f"IQR = {iqr(tiempos)}")

# 🧩 Ejercicio 4: Detección formal de valores atípicos

# Sabiendo que Q_3 = 22$ e $IQR = 7$, calcula el Límite Superior (Q_3 + 1.5 * IQR$).

limite_sup = tiempos_q3 + (1.5 * iqr(tiempos))

print(f"Límite superior = {limite_sup}")

# ¿Qué tiempos de nuestra lista ([12, 14, 15, 15, 16, 18, 20, 22, 45, 50]) superan ese límite y quedan confirmados matemáticamente como valores atípicos?

atipicos_sup = []
for t in tiempos:
    if t > limite_sup:
        atipicos_sup.append(t)

print(f"Los tiempos atipicos por encima de la mediana son: {atipicos_sup[0]} y {atipicos_sup[1]}")