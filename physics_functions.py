"""
Use functions to convert temperatures, calculate force, energy, and work.

- Create `f_to_c()` to convert Fahrenheit to Celsius.
- Create `c_to_f()` to convert Celsius to Fahrenheit.
- Create `get_force()` to return mass times acceleration.
- Create `get_energy()` to return mass times the speed of light squared.
- Create `get_work()` to return force times distance, using `get_force()` inside it.

Test your functions with the provided values and print the results.
"""

rain_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below:

#Convierte Fahrenheit en Celsius 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

#¡Vamos a probar la función!
f100_in_celsius = f_to_c(100)

#Esta hace lo contrario
def c_to_f(c_temp):
  f_temp = c_temp * (9 / 5) + 32
  return f_temp

#¡Otra!
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies", train_force, "Newtons of force.")

def get_energy(mass, c = 3 * 10 ** 8):
  return (mass * c) ** 2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", str(train_work), "Joules of work over", str(train_distance), "meters")
