# Vamos a volver al contexto del taller de bicicletas, pero esta vez tenemos más información.

# Durante una semana se registraron 100 reparaciones:

# Tipo de reparación	Nº reparaciones
# Pinchazo	            35
# Frenos	            20
# Transmisión	        15
# Ruedas	            10
# Suspensión	        8
# Eléctrica	            7
# Otras	                5
# Total	                100

# ¿Qué probabilidad hay de que sea una reparación de frenos?

# ¿Cuántos casos favorables tenemos? 20
# ¿Cuántos casos posibles? 100

# Calcula la probabilidad:

# como fracción: 20/100
# como decimal: 0.2
# como porcentaje: 20%

# Ahora sí: Python

total_reparaciones = 100
frenos = 20
pinchazo = 35
frenos = 20
transmision	= 15
ruedas = 10
suspension = 8
electrica = 7
otras = 5

probabilidad_frenos = frenos / total_reparaciones

# Conviértela en porcentaje:

probabilidad_frenos = probabilidad_frenos * 100

# ¿Por qué para obtener el porcentaje tenemos que multiplicar la probabilidad por 100?
# Es la ecuación resultante de una regla de tres. En el ejemplo, 20 = x y 1 = 100, por lo tanto x = 20 * 100

# ¿Qué probabilidad hay de que una reparación elegida al azar NO sea de frenos?

probabilidad_frenos = frenos / total_reparaciones
prob_no_frenos = (total_reparaciones - frenos) / total_reparaciones

prob_no_frenos + probabilidad_frenos == 1

# Un compañero afirma:
# "Si elegimos una reparación al azar, es más probable que sea de transmisión que de ruedas y suspensión juntas."

# ¿Tiene razón?

# Quiero que respondas:

# Probabilidad de transmisión:
prob_trans = transmision / total_reparaciones

# Probabilidad de ruedas o suspensión:
prob_ruedas_susp = (ruedas + suspension) / total_reparaciones

# Comparación:
compañero = ""
if prob_trans > prob_ruedas_susp:
    compañero = "ha acertado"
else:
    compañero = "no sabe estadística"
print(f"Mi compañero {compañero}")

# Conclusión en lenguaje normal:
# La probabilidad de que sea transmisión es del 15% frente al 18% que supone que toque ruedas o suspensión. 
# Mi compañero se equivoca, siendo más probable que cojamos una suspensión o unas ruedas frente a una transmisión.

# Imagina ahora otro escenario. Tenemos 100 clientes del taller:

# 30 tienen una bicicleta de carretera.
# 20 tienen una bicicleta de gravel.
# 10 tienen ambas.

# Un compañero dice:
# "La probabilidad de que un cliente tenga carretera o gravel es 30% + 20% = 50%."

# ¿Tiene razón?

# Sin buscar nada y sin Python todavía:

# Explica por qué el 50% podría estar contando algo dos veces:
# Esta contando también a los que tienen ambas cosas. A ese 10%. 

# Calcula cuál crees que debería ser la probabilidad correcta:
# Habría que restar a ese 10% que tiene ambas cosas. 40%

# Intenta escribir una fórmula general en Python:
# Prob_road_or_gravel = prob_gravel + prob_road - prob_road_and_gravel

# Quiero que pienses en esta situación:
# De los 100 clientes, sabemos que 30 tienen bicicleta de carretera.
# De esos 30, 10 también tienen gravel.

# Un compañero pregunta:
# "Si sé que un cliente tiene carretera, ¿cuál es la probabilidad de que también tenga gravel?"

# ¿Qué debería ser el total que utilizamos como referencia: 100 clientes o los 30 de carretera?
# ¿Cuál crees que es la probabilidad?

# Explícame con tus palabras por qué:
# La muestra cambia, para este calculo el resto de clientes (los que no tienen carretera) no nos importan. 
# La probabilidad seria si 30 es 1, 10 es x. x = 10 / 30 = 0.33 = 33.3 %

# Tenemos otra vez los 100 clientes:

# 30 carretera
# 20 gravel
# 10 ambas

# A. ¿Cuál es la probabilidad de que un cliente tenga gravel?
# B. ¿Cuál es la probabilidad de que un cliente tenga gravel sabiendo que tiene carretera?

# El cálculo de A:
# p_gravel = gravel / total, 20%

# El cálculo de B:
# p_carretera_and_gravel = ambas / carretera 

# Una frase explicando por qué los denominadores son diferentes:
# Como hemos observado antes, la muestra a coger para el calculo cambia. 
# En una nos interesa el total, en la otra partimos de las personas que tienen carretera

# Un compañero dice:
# "Si la probabilidad de que un cliente tenga gravel es 20%, entonces la probabilidad de que tenga gravel sabiendo que tiene carretera también debería ser 20%."

# ¿Estás de acuerdo o no?
# No ¿Ves como tengo raźon y mi compañero no sabe estadística?. El número de clientes que tiene ambas es 10. Eso no cambia. 
# En la primera afirmación la muestra son 100 clientes, en la segunda son 30.
# En la primera 20 sobre 100. En la segunda 10 sobre 30.

total_clientes = 100
carretera = 30
gravel = 20
ambas = 10

p_gravel = gravel / total_clientes
p_gravel_dado_carretera = ambas / carretera

print(f"La probabilidad de que un cliente tenga gravel es de {p_gravel * 100}%")
print(f"La probabilidad de que un cliente tenga gravel sabiendo que tiene carretera es de {p_gravel_dado_carretera * 100:1f}%")

# ¿Es mayor la probabilidad de gravel sabiendo que tiene carretera que la probabilidad general de gravel?
print(p_gravel_dado_carretera > p_gravel)

# Tenemos estos datos de 200 reparaciones:

# Tipo	        Nº reparaciones
# Pinchazo	    70
# Frenos	    50
# Transmisión	30
# Ruedas	    25
# Suspensión	15
# Eléctrica	    10

# Y sabemos que de las 50 reparaciones de frenos, 20 fueron realizadas en bicicletas eléctricas.

# ¿Cuál es la probabilidad de que una reparación elegida al azar sea de frenos?
# p_frenos = frenos / total_reparaciones = 50%

# ¿Cuál es la probabilidad de que sea de frenos sabiendo que la bicicleta es eléctrica?
# Me falta conocer que cantidad de reparaciones existen de frenos & electricas
# Tenemos la muestra, pero no el numerador