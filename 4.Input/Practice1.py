#1
#Use a=3, b=-5, c=2

from math import sqrt

a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

if(pow(b,2)-4*a*c < 0):
    print('No se puede realizar')
else:
    x1 = (-b + sqrt((pow(b, 2) - 4*a*c))) / (2*a)
    x2 = (-b - sqrt((pow(b, 2) - 4*a*c))) / (2*a)
    print('La solucion es: x1=' + str(x1) + ', x2=' + str(x2))

#2

practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingrese el valor de la practica 2: '))
practica3 = float(input('Ingrese el valor de la practica 3: '))

ExamenParcial = float(input('Ingrese el valor del examen parcial: '))
ExamenFinal = float(input('Ingrese el valor del examen final: '))

promedioPractica = (practica1 + practica2 + practica3)/3

promedioFinal = (promedioPractica + 2*ExamenParcial + 3*ExamenFinal)/6

print('El promedio final del estudiante es: ' + str(promedioFinal))