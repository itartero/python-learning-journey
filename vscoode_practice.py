name = "Nacho"
print(name.capitalize())
age = 38
print(age)

def age_calculated(name, age):
    birth_year = 2026 - age
    print(f"Hola! Soy {name} y tengo {age} años. Nací en el año {birth_year}")

age_calculated("Nacho", 38)