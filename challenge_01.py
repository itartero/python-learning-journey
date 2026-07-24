#Se te dan dos números almacenados en num1 y num2. Si la suma de num1 y num2 NO es igual a 10, entonces guarda True en una variable llamada not_ten; en caso contrario, guarda False en not_ten.

num1 = 6
num2 = 3

# Write your if statement here

if num1 + num2 != 10:
  not_ten = True
else: 
  not_ten = False

# Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten))
