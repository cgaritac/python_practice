#1:
list = []
even = []
odd = []

def data():
    for i in range(5):
        x = int(input('Por favor ingrese un numero: '))
        list.append(x)

def order():
    for i in list:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()

def showData():
    print('Pares: {}'.format(even))
    print('Impares: {}'.format(odd))

data()
order()
showData()

#2
number = int(input('Ingrese un nuemero entero: '))

def factorial():
    result = 1
    for i in range(1, number + 1):
        print(i)
        result = i*result
    print('El resultado es: {}'.format(result))

factorial()

#3
def numeros():
    number1 = int(input('Ingrese el numero 1: '))
    number2 = int(input('Ingrese el numero 2: '))

    if number1>number2:
        return 1
    elif number1<number2:
        return -1
    else:
        return 0

print(numeros())

#4
def calcIVA():
    cantidad = float(input('Ingrese la cantidad: '))
    iva = input('Ingrese porcentaje de IVA: ')

    if iva == '' or iva == '0':
        iva = 21
    if int(iva) < 0:
        return 'No se puede resolver para negativos'
    iva = int(iva)
    return cantidad*iva/100 + cantidad

print(calcIVA())

#5
def cuadrado(base, altura):
    return base * altura

def circulo(radio):
    return 3.14 * pow(radio, 2)

print(cuadrado(2,3), circulo(3))

#6
def medidaLista(*numeros):
    return len(numeros)

print(medidaLista(1,4,3,7,3,8,9,4,4,4,5,6))