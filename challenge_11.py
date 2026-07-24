# Escribe una función llamada append_size() que reciba una lista como argumento. La función debe calcular cuántos elementos tiene esa lista, añadir ese número al final y devolver la lista resultante. Por ejemplo, si recibe [23, 42, 108], debería devolver [23, 42, 108, 3].

# Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
