cadena = 'Este es un sonido de lluvia'
cadena2 = ''

print(cadena[:2])
print(cadena[len(cadena)-3:len(cadena)])
print(cadena[-3:])

for i in range(len(cadena)-1):
    if i % 2 == 0:
        cadena2 = cadena2 + cadena[i]
print(cadena2)

cadena2 = ''

for i in range(len(cadena)-1 , -1, -1):
    cadena2 = cadena2 + cadena[i]

print(cadena2)

cadena2 = ''

cadena2 = cadena[::-1]

print(cadena2)

cadena2 = ''

cadena2 = ''.join(reversed(cadena))

print(cadena2)

cadena2 = ''

print(cadena+cadena[::-1])