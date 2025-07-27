class Animales():
    def habla(self):
        print('Yo soy un animal')
    
    def descripcion(self):
        print('Yo soy un {}'.format(self.animal))

class Perro(Animales): #Asi se hace la herencia en python
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()

animal.habla()

perro = Perro()

perro.habla()

abeja = Abeja('Abeja')
abeja.descripcion()