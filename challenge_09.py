# Escribe una función llamada movie_review() que reciba una puntuación. Si la nota es 5 o menos, debe devolver "Avoid at all costs!". Si está por encima de 5 pero todavía por debajo de 9, debe devolver "This one was fun.". Y si la puntuación es 9 o mayor, debe devolver "Outstanding!".

# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

# Uncomment these function calls to test your movie_review function:
#print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
#print(movie_review(6))
# should print "This one was fun."
