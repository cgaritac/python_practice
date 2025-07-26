class FabricaTelefonos():
    #Un asterisco es para tuplas y dos asteriscos es para diccionarios
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos('Alcatel', 'Negro', 'Azul', m1 = 500, m2 = 1000)

print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

#Atributos temporales
telefono.memoria = 512
print(telefono.memoria)