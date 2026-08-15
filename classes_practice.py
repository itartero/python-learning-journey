# Proyecto de práctica de Programación Orientada a Objetos (OOP) en Python.
# Se ha creado un sistema de clases para organizar menús, franquicias y
# diferentes negocios de restauración.
#
# El proyecto incluye:
# - Clase Menu para gestionar productos, precios, horarios y calcular facturas.
# - Clase Franchise para gestionar restaurantes, direcciones y menús disponibles
#   según la hora.
# - Clase Business para agrupar diferentes franquicias.
# - Creación de varios menús y franquicias para dos negocios diferentes.
#
# Objetivo: practicar clases, objetos, atributos, métodos, listas, diccionarios
# y la relación entre diferentes objetos en Python.

import datetime as dt

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return f"El menú {self.name} se sirve entre las {self.start_time} y las {self.end_time}"

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in self.items:
      if item in purchased_items:
        bill += self.items[item]
      else:
        pass
    return bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu)
    return available

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchise = franchises

brunch = Menu("Brunch", {'pancakes':7.50, 'waffles':9.00, 'burger':11.00, 'home fries':4.50, 'coffee':1.50, 'expresso':3.00, 'tea':1.00, 'mimosa':10.50, 'orange juice':3.50}, dt.time(11, 0), dt.time(16, 0))

early_bird = Menu("Early Bird", {'salumeria plate':8.00, 'salad and breadsticks(serves 2, no refills)':14.00, 'pizza with quattro formaggi':9.00, 'duck ragu':17.50, 'mushroom ravioli(vegan)':13.50, 'coffee':1.50, 'expresso':3.00}, dt.time(15, 0), dt.time(18, 0))

dinner = Menu("Dinner", {'crostini with eggplant caponata':13.00, 'caesar salad':16.00, 'pizza with quattro formaggi':11.00, 'duck ragu':19.50, 'mushroom ravioli (vegan)':13.50}, dt.time(17, 0), dt.time(23,00))

kids = Menu("Kids", {'chicken nuggets':6.50, 'fusilli with wild mushrooms':12.00, 'apple juice':3.00}, dt.time(11, 0), dt.time(21, 0))

arepas_menu = Menu("Take a'Arepa", {'arepa pabellon':7.00, 'pernil arepa':8.50, 'guayanes arepa':8.00, 'jamon arepa':7.50}, dt.time(10, 0), dt.time(20, 0))

print(brunch)
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli(vegan)"]))

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

print(flagship_store.available_menus(dt.time(17, 0)))

restaurant = Business("Basta Fazoolin' with My Heart", [flagship_store, new_installment])

arepas = Business("Take a' Arepa", [arepas_place])
