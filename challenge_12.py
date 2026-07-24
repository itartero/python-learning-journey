# Crea una función llamada append_sum() que reciba una lista como parámetro. La función debe tomar los dos últimos valores de la lista, sumarlos y añadir el resultado al final. Tiene que repetir ese proceso tres veces y después devolver la lista resultante. Por ejemplo, si empieza con [1, 1, 2], al final debería devolver [1, 1, 2, 3, 5, 8].

# Write your function here
def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
