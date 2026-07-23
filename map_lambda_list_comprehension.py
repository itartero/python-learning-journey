#Usa map() para convertir los elementos de str_numbers en enteros y almacenar el resultado en convert_int.

#Usa map() junto con una lambda para sumar elemento a elemento las listas list_a y list_b, guardando el resultado en convert_sum.

#Usa una list comprehension para calcular el cuadrado de cada número de numbers y guardarlo en convert_square.

str_numbers = ["10", "20", "30", "40", "50"]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
numbers = [2, 4, 6, 8, 10]

# write your code below
convert_int = list(map(int, str_numbers))
print(convert_int)

convert_sum = list(map(lambda a_number, b_number: a_number + b_number, list_a, list_b))
print(convert_sum)

convert_square = [nums ** 2 for nums in numbers]
print(convert_square)
