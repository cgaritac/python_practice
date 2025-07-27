class A():
    def __init__(self):
        self._contador = 0 #La forma moderna de encapsular atributos en python es mediante un solo guion bajo
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()