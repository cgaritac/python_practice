class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    @property #Esto se agrega para que el metodo get cuando se llama no ocupe que se pongan los parentesis al final
    def cuenta(self): #Esto es un metodo get
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador

a = A()

print(a.cuenta)
print(a.contador)

