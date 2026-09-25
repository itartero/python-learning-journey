# En este ejercicio busco practicar Python con los conceptos estádisticos aprendidos intentando no utilizar librerias o las menos posibles

import math

# Calculamos la media
def media(datos):
    media_t = sum(datos) / len(datos)
    return media_t

# Calculamos la mediana
def mediana(datos):
    datos = sorted(datos)
    if len(datos) % 2 == 0:
        mediana_t = ((datos[(len(datos) // 2) - 1]) + (datos[len(datos) // 2])) / 2
    else:
        mediana_t = datos[len(datos) // 2]
    return mediana_t

# Calculamos la desviación estándar
def desv(datos):
    desv_t = 0
    for t in datos:
        desv_t += (t - media(datos)) ** 2
    desv_t = math.sqrt(desv_t / len(datos))
    return desv_t

# Extraemos los percentiles. Q2 es la mediana, ya esta calculado
# Extraemos Q1
def cuartil_1(datos):
    datos = sorted(datos)
    valores_q1 =[]
    q1 = 0
    if len(datos) % 2 == 0:
        for i in range(len(datos)):
            if i < len(datos) / 2:
                valores_q1.append(datos[i])
    else:
        for i in range(len(datos)):
                    if i < len(datos) // 2:
                        valores_q1.append(datos[i])
    if len(valores_q1) % 2 == 0:
        q1 = ((valores_q1[(len(valores_q1) // 2) - 1]) + (valores_q1[len(valores_q1) // 2])) / 2
    else:
        q1 = valores_q1[len(valores_q1) // 2]
    return q1

# Extraemos Q3
def cuartil_3(datos):
    datos = sorted(datos)
    valores_q3 =[]
    q3 = 0
    if len(datos) % 2 == 0:
            for i in range(len(datos)):
                if i >= len(datos) / 2:
                    valores_q3.append(datos[i])
    else:
        for i in range(len(datos)):
                if i > len(datos) // 2:
                    valores_q3.append(datos[i])
    if len(valores_q3) % 2 == 0:
        q3 = ((valores_q3[(len(valores_q3) // 2) - 1]) + (valores_q3[len(valores_q3) // 2])) / 2
    else:
        q3 = valores_q3[len(valores_q3) // 2]
    return q3

# Calculamos IQR
def iqr(datos):
    datos_iqr = cuartil_3(datos) - cuartil_1(datos)
    return datos_iqr

# Calculamos límites matemáticos superior e inferior 
def lim(datos):
    limites = []
    limites.append(cuartil_1(datos) - (iqr(datos) * 1.5))
    limites.append(cuartil_3(datos) + (iqr(datos) * 1.5))
    return limites

# Extraemos los valores atípicos
def atipicos(datos):
    atipicos = []
    for dato in datos:
        if dato < lim(datos)[0] or dato > lim(datos)[1]:
            atipicos.append(dato)
    return atipicos

# Esta función extrae media, mediana, desviación estándar, cuartiles, IQR, limites (superior e inferior) y los valores atipicos y les da formato
def informe_distribucion(datos):
    print(f"Media = {media(datos)}")
    print(f"Mediana = {mediana(datos)}")
    print(f"Desviación Estándar = {desv(datos)}")
    print(f"Q1 = {cuartil_1(datos)}")
    print(f"Q2 = {mediana(datos)}")
    print(f"Q3 = {cuartil_3(datos)}")
    print(f"IQR = {iqr(datos)}")
    print(f"Límite Inferior = {lim(datos)[0]}")
    print(f"Límite Superior = {lim(datos)[1]}")
    print(f"Valores Atípicos = {atipicos(datos)}")

informe_distribucion([10, 15, 20, 20, 20, 25, 30])