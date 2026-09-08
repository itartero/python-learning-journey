# Media = 49
# Mediana = 44'5

# No, no representa bien el tiempo normal. Existen valores atipicos que distorsionan la media.
# El 91 hace crecer la media
# Quizas la mediana se ajuste mejor a los datos reales.

tiempos = [42, 45, 43, 47, 44, 46, 45, 43, 44, 91]

media = sum(tiempos) / len(tiempos)
mediana = sorted(tiempos)
if len(mediana) % 2 == 0:
    mediana = (mediana[len(mediana) // 2 - 1] + mediana[len(mediana) // 2]) / 2
else:
    mediana = mediana[len(mediana) // 2]

maximo = max(tiempos)
minimo = min(tiempos)
rango = maximo - minimo

print(media)
print(mediana)
print(maximo)
print(minimo)
print(rango)

# Los técnicos han trabajado de manera muy parecida ejecutando la tarea en un tiempo muy similar.
# Solo ha aparecico un valor atípico que ha distorsionado la media.
# Puede haberse debido a un error en la introducción, en el calculo o falta de repuesto.