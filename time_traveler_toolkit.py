# Importamos todos las funciones necesarias
from custom_module import generate_time_travel_message
import datetime as dt
from decimal import Decimal
from random import randint
from random import choice 

# Definimos las variables practicando funciones de datetime y random
fecha_p = dt.date.today()
hora_p = dt.datetime.now().time()
year = randint(-5000, 2042)
target_years = ["Madrid", "Alemania", "Austria", "Cuba"]
target = choice(target_years)
welcome = f"Son las {hora_p} del día {fecha_p}."

print(welcome)

# Definimos el coste del viaje por año. Descubriendo tambien 'abs'
base_cost = Decimal("13.90")
cost = round(base_cost * abs(dt.date.today().year - year))

print(generate_time_travel_message(year, target, cost))
