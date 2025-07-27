class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0 #Cuando se agrega doble guion bajo a un atributo al inicio se encapsula que es
                            # similar a volverlo privado, solo se puede acceder desde la misma clase
    
    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador

print('Objeto 1')

a = A()

print(a.cuenta())

a.incrementar()

print(a.cuenta())

print(a.contador) #Esto no se deberia hacer

print('Objeto 2')

b = B()

print(b.cuenta())

b.incrementar()

print(b.cuenta())

print(b.__contador)