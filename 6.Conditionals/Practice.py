#1:

letra = input('Ingrese una letra: ')

vocales = ['a', 'e', 'i', 'o', 'u']

for i in vocales:
    if letra.lower() == i:
        print('Es vocal')
        break
    elif i == vocales[len(vocales)-1]:
        print('No es vocal')
        break
    # else:
    #     print('No es vocal')
    #     break

if letra.lower() in 'aeiou':
    print('Es una vocal')
else:
    print('No es una vocal')


#2:

numero = int(input('Ingrese un numero entero: '))

if numero<0:
    numero = numero*-1
    print(numero)
else:
    print(numero)

#3:

word1 = input('Ingrese la palabra 1: ')
word2 = input('Ingrese la palabra 2: ')

if word1[-3:] == word2[-3:]:
    print('Si riman')
elif word1[-2:] == word2[-2:]:
    print('Riman un poquito')
else:
    print('No riman')

#4:

candidato = {
    'A': 'Rojo',
    'B': 'Verde',
    'C': 'Azul'
}

seleccion = input('Vote por el candidato: ')

print('Usted ha votado por el partido {}'.format(candidato[seleccion.upper()]))