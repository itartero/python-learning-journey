#Se te da un presupuesto mensual y algunos gastos, y necesitas comprobar si la suma de los gastos supera el presupuesto.
#Primero, guarda el total de todos los gastos en una variable llamada total.
#Después, comprueba si el total es mayor que el presupuesto. Si lo es, guarda True en una variable llamada over_budget; en caso contrario, guarda False en over_budget.

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
  over_budget = True
else:
  over_budget = False

# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))
