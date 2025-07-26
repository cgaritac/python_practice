#1:
numero = int(input('Ingrese un numero entero: '))

contador = 0

while(contador < 10):
    print('{} X {} = {}'.format(numero, contador, numero*contador))
    contador += 1


#2: 
edad = int(input('Ingrese su edad: '))

contador = 0

while(contador < edad):
    print('Ano cumplido #{}'.format(contador + 1))
    contador += 1
