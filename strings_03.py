# Procesar una cadena con poemas destacados para convertirla en una estructura más fácil de usar.
# Primero se separan los poemas en una lista, luego se limpian los espacios sobrantes y después se divide
# cada entrada en título, autor y fecha. Finalmente, se guardan esos datos en listas separadas y se
# formatea cada poema para mostrarlo con el texto: "El poema TITLE fue publicado por POET en DATE."

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")

highlighted_poems_stripped = [poem.strip() for poem in highlighted_poems_list]

highlighted_poems_details = [poem_strip.split(":") for poem_strip in highlighted_poems_stripped]

titles = []
poets = []
dates = []

for data in highlighted_poems_details:
  titles.append(data[0])
  poets.append(data[1])
  dates.append(data[2])

for i in range(len(titles)):
  print("The poem {} was published by {} in {}".format(titles[i], poets[i], dates[i]))