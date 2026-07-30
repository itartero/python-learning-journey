#El objetivo del ejercicio es descifrar un mensaje cifrado mediante un cifrado César, que consiste en desplazar las letras del alfabeto un número fijo de posiciones. Para ello, se recorre cada carácter del mensaje cifrado y, si pertenece al alfabeto, se busca su posición y se sustituye por la letra correspondiente aplicando un desplazamiento (offset) de 10 posiciones hacia atrás. Si el carácter no es una letra (espacios, signos, etc.), se mantiene sin cambios.

#Además, se implementa una función genérica (encode_function) que permite aplicar este mismo proceso a cualquier mensaje y con cualquier desplazamiento indicado. Por último, se crea una función adicional (ultradecoder_function) que prueba automáticamente todos los posibles desplazamientos (del 1 al 26) para mostrar todas las posibles decodificaciones, lo que permite identificar el mensaje correcto cuando no se conoce el offset.

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

decipher_message = ""
# Iterar por cada una de las letras del mensaje cifrado
for character in cipher_message:
  # Vamos a comprobar si se trata de una letra dentro de "alphabet". Si esta dentro cogemos su [index + 10] y la agregamos a una nueva lista
  if character in alphabet:
    for index in range(len(alphabet)):
      if character == alphabet[index]:
        # [index + 10] daria error. 26 - 10 = 16, restandolo llegamos a la misma letra
        decipher_message += alphabet[index - 16]
  # Si el caracter no es una letra se deja tal cual
  else:
    decipher_message += character

# Para devolver el mensaje cifrado, una función que haga el mismo proceso del revés definiendo el mensaje y el offset de las letras elegido
def encode_function(my_message, offset):
  new_decode_message = ""
  for character in my_message:
    if character in alphabet:
      for index in range(len(alphabet)):
        if character == alphabet[index]:
          new_decode_message += alphabet[index - offset]
    else:
      new_decode_message += character
  return new_decode_message

# He creado esta función para que sin saber el offset imprima los 26 resultados y pueda identificar cual es el correcto (No se si era esto lo que pretendia el ejercicio o hay una forma más elegante)
def ultradecoder_function(my_message):
  for offset in range(1, 27):
    new_decode_message = ""
    for character in my_message:
      if character in alphabet:
        for index in range(len(alphabet)):
          if character == alphabet[index]:
            new_decode_message += alphabet[(index - offset)]
      else:
        new_decode_message += character
    print(new_decode_message)
