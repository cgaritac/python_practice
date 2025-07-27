class Animales():
    def __init__(self, nombre):
        self.nombre = nombre
    
class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre)
        self.sonido = sonido

perro = Perro('Firulais', 'Guau!')

print(perro.nombre)
print(perro.sonido)