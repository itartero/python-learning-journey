def purchase_100(sales):
    # Esta función devuelve el número de compras que superen un importe de 100
    sum_100 = 0
    # Iteramos en cada una de las listas que contiene sales
    for sale in sales:
        total_sale = 0
        # Volvemos a iterar en cada una de los importes de cada compra
        for price in sale:
            # Sumamos los importes y los almacenamos en una variable
            total_sale += price
        # Comprobamos si es mayor a 100, si lo es sumamos 1 al resultado de la función
        if total_sale >= 100:
            sum_100 += 1
    # Devolvemos el valor de la suma de compras que superen los 100
    return sum_100

sales = [
    [20, 30, 60],
    [10, 15],
    [50, 50],
    [120]
]
print(purchase_100(sales))
