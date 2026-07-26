# Tu jefe de la organización de poesía te ha enviado una lista con nombres de autores para prepararla para la base de datos. Por desgracia, te la mandó como una sola cadena larga, con los nombres separados por comas.
# Usando  .split()  y la cadena proporcionada, crea una lista llamada  author_names  que contenga cada nombre de autor como una cadena independiente.
# Ahora resulta que no querían los nombres de pila de los poetas, sino solo sus apellidos.
# Crea otra lista llamada  author_last_names  que contenga únicamente los apellidos de los autores incluidos en la cadena proporcionada.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

print(author_names)

def extract_last(author_names):
  author_last_names = []
  for author in author_names:
    author_last_names.append(author.split()[-1])
  return author_last_names
    
print(extract_last)
