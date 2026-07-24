# Crea una función llamada always_false() que reciba un parámetro llamado num.
# Usando una condición if, la variable num y los operadores > y <, consigue que la función devuelva False sin importar qué número tenga num.
# Una condición if que nunca puede cumplirse se llama contradicción. No se suele usar mucho, pero es importante saber que se puede hacer.

# Write your always_false function here:
def always_false(num):
  if num > num:
    return True
  return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
