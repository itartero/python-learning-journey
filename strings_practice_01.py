# Esta función coge las tres primeras letras del nombre y las 4 primeras del apellido para concatenarlas y crear un nombre de usuario. 
# Si tienen menos letras de las que son necesarias, escoge todo
def username_generator(first_name, last_name):
  user_name = ""
  length_f = len(first_name)
  length_l = len(last_name)
  if length_f > 3 and length_l > 4:
    user_name = first_name[:3] + last_name[:4]
  elif length_f <= 3 and length_l > 4:
    user_name = first_name + last_name[:4]
  elif length_f > 3 and length_l <= 4:
    user_name = first_name[:3] + last_name
  else:
    user_name = first_name + last_name
  return user_name

# En esta función se genera una contraseña moviendo todas las letras de user_name a la derecha, siendo la última la primera letra.  
def password_generator(user_name):
  password = ""
  # "password = user_name[-1] + user_name[:-1]"
  # "return password" Esta sería otra manera de hacerlo
  for index in range(0, len(user_name)):
    password += user_name[index - 1]
  return password
