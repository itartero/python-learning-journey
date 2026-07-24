#Define una función llamada large_power() con dos parámetros, base y exponent. La función debe devolver True si base elevado a exponent es mayor que 5000; en caso contrario, debe devolver False.

# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
