def argumento(num):
    return type(num)

print(argumento(5))


#Para hacer que el valor se almacene como una tupla, se le pone un asterisco
def argumento(*num):
    return type(num)

print(argumento(5))