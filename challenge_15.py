# Escribe una función llamada combine_sort() que reciba dos listas. La función debe juntar los elementos de ambas en una nueva lista, ordenar esa lista de menor a mayor y devolver el resultado final.

# Write your function here
def combine_sort(my_list1, my_list2):
  return sorted(my_list1 + my_list2) 

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
