# Limpiar cada línea del poema eliminando espacios sobrantes y unirlas después en un solo texto multilínea.
# Finalmente, imprimir el poema completo con cada verso en su propia línea.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = [(line.strip()) for line in love_maybe_lines]

love_maybe_full = "\n".join(love_maybe_lines_stripped)

print(love_maybe_full)