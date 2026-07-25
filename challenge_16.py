# Crea una función llamada  divisible_by_ten()  que reciba como parámetro una lista de números llamada  nums.
# La función debe devolver cuántos números de la lista son divisibles entre 10.

#Write your function here
def divisible_by_ten(nums):
  divisible_by_ten_count = 0
  for num in nums:
    if num % 10 == 0:
      divisible_by_ten_count += 1
  return divisible_by_ten_count


#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
