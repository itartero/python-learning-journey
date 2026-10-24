import random
random.seed(42)

bicicletas = {"bici_01":[], "bici_02":[], "bici_03":[]}

for bici in bicicletas:
    for i in range(random.randint(4,6)):
        ruta = (f"R{i + 1}", round(random.uniform(10.0, 50.0), 1), random.randint(30, 120))
        bicicletas[bici].append(ruta)

print(bicicletas)