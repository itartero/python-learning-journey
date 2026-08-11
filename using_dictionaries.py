# Este ejercicio practica el uso de diccionarios en Python.
# Primero se crea un diccionario vacío llamado "reading".
# Después, se extraen con pop() los elementos 6, 14 y 8
# del diccionario "elements", guardándolos como catalyst, core
# y byproduct, respectivamente.
# Finalmente, se recorren los pares clave-valor de "reading"
# para mostrar una frase con cada elemento.

elements = {
    1: "Hydrogen",
    2: "Helium",
    3: "Lithium",
    4: "Beryllium",
    5: "Boron",
    6: "Carbon",
    7: "Nitrogen",
    8: "Oxygen",
    9: "Fluorine",
    10: "Neon",
    11: "Sodium",
    12: "Magnesium",
    13: "Aluminum",
    14: "Silicon",
    15: "Phosphorus",
    16: "Sulfur",
    17: "Chlorine",
    18: "Argon",
    19: "Potassium",
    20: "Calcium",
    21: "Scandium",
    22: "Titanium"
}

reading = {}

reading["catalyst"] = elements.pop(6, 0)
reading["core"] = elements.pop(14, 0)
reading["byproduct"] = elements.pop(8, 0)

for read, element in reading.items():
    print("Your", read, "element is", element + ".")
