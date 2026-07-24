# Escribe una función llamada twice_as_large() que reciba num1 y num2. Devuelve True si num1 es mayor que el doble de num2; en caso contrario, devuelve False.

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
