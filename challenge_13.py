# Crea una función llamada larger_list() que reciba dos listas. La función debe comprobar cuál de las dos tiene más elementos y devolver el último valor de esa lista. Si ambas tienen el mismo tamaño, debe devolver el último elemento de my_list1.

# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) == len(my_list2):
    return my_list1[-1]
  if len(my_list1) > len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
