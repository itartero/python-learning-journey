# Define una función llamada max_num() que reciba tres números. Devuelve el mayor de ellos y, si el valor más alto se repite, devuelve "It's a tie!".

# Write your max_num function here:
def max_num(num1, num2, num3):
  if (num1 == num2 or num1 == num3 or num2 == num3):
    return "It's a tie!"
  return max(num1, num2, num3)



# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
