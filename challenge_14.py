# Escribe una función llamada more_than_n() que reciba una lista, un elemento y un número. La función debe contar cuántas veces aparece ese elemento en la lista y devolver True si aparece más de n veces. En caso contrario, debe devolver False.

# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1], 2, 3))
