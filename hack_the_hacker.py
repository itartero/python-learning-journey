# Ejercicio de manipulación de archivos en Python
# El programa lee un archivo CSV con usuarios y contraseñas
# Extrae los nombres de los usuarios comprometidos
# Genera un archivo de texto con ellos, crea un mensaje en formato JSON
# Escribe una firma ASCII en el archivo de contraseñas

import csv
import json

compromised_users = []
# Vamos a sacar una lista de todos los usuarios que se han visto comprometidos por la filtracion
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  password_row = {}
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

# Pasamos esa lista a un archivo txt
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

# Creamos y manipulamos un archivo json para informar a un superior
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient':'The Boss', 'message':'Mission Success'}
  json.dump(boss_message_dict, boss_message)

# Modificamos el archivo original para engañar al hacker y crear una manipulación de falsa bandera
slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

with open('passwords.csv', 'w') as new_passwords_obj:
  new_passwords_obj.write(slash_null_sig)
