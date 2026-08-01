alphabet = "abcdefghijklmnopqrstuvwxyz"

def vigenere_message(message, key):
  decode_index = "" 
  key_message = ""
  index = 0
  for character_m in message:
    if character_m in alphabet:
      key_message += key[index]
      index += 1
      if index >= len(key):
        index = 0
    else:
      key_message += character_m
  # Hasta aqui, tengo la cadena "key_message", equivalente en longitud a 'message' con los valores de 'key'
  message_index = []
  for character_m in message:
    if character_m in alphabet:
      message_index.append(alphabet.find(character_m))
    else:
      message_index.append(character_m)
  # He creado "message_index" para poder almacenar en una lista los index de "message". Y hago lo mismo con "key_message" a continuación
  key_index = []
  for character_k in key_message:
    if character_k in alphabet:
      key_index.append(alphabet.find(character_k))
    else:
      key_index.append(character_k)
  # Ahora creo una nueva lista 'decode_index' haciendo la resta de ""message_index" y ""key_index"
  index = 0
  decode_index = []
  for index_number in message_index:
    if index_number not in (" ", "?", "!"):
      decode_index.append((index_number - key_index[index]) % 26)
    else:
      decode_index.append(index_number)
    index += 1
  # Ahora iteramos por cada una de los index de la lista y vamos asignando la letra de 'alphabet' que le toca en 'decode_message'
  decode_message = []
  for i in decode_index:
    if i not in (" ", "?", "!"):
      decode_message.append(alphabet[i])
    else:
      decode_message.append(i)
  print(decode_message)

print(vigenere_message("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!", "friends"))
