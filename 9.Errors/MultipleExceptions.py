while True:
    try:
        num1 = int(input('Ingresa un numero: '))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print('No se puede dividir entre cero')


while True:
    try:
        edad = int(input('Ingrese su edad: '))
        print('Tu edad es: ', edad)
        break
    except ValueError:
        print('Ingresaste un valor erroneo')

while True:
    try:
        edad = int(input('Ingrese su edad: '))
        print('Tu edad es: ', edad)
        break
    except KeyboardInterrupt:
        print('\nHas cancelado la ejecucion')
        break