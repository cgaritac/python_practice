def entero():
    print('Este es un numero entero')
    return 10

def decimal():
    print('Este es un numero decimal')
    return 9.99

def asignacion():
    return 1,2,3,4,5

print(entero())
decimal()
print(decimal())

a,b,c,d,e = asignacion()

print(a)
print(b)