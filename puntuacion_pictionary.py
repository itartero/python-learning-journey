letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

# Creamos un diccionario iterando por las dos listas combinadas con zip
  # letter_to_points = {letter:point for letter, point in zip(letters, points)}

# Una versión más completa que tiene en cuenta palabras minusculas
letter_to_points = {}

for letter, point in zip(letters,points):
  letter_to_points[letter.upper()] = point
  letter_to_points[letter.lower()] = point

print(letter_to_points)

# Esta función coge una palabra y suma los puntos de cada una de sus letras
word = ""
def score_word(word):
  point_total = 0
  for ch in word:
    if ch in letter_to_points:
      point_total += letter_to_points[ch]
    else:
      point_total += 0
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

# Creamos un diccionario donde almacenamos cada una de las palabras jugadas por cada jugador
player_to_words = {"player1": ["BLUE","TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

# Calculamos la puntuación de cada palabra y vamos almacenando su valor en una variable para traspasarala al diccionario vacio player_to_points
for player in player_to_words:
  player_points = 0
  for word in player_to_words[player]:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

# Función que añade palabras a la jugada de un jugador
def play_word(player, word):
  player_to_words[player].append(word)

