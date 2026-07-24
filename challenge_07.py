# Crea una función llamada same_name() que reciba dos parámetros: your_name y my_name.
# Si ambos nombres son idénticos, la función debe devolver True. En caso contrario, debe devolver False.

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  return False

# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False
