class FabricaTelefonos():
    marca = 'Samsung'

    def elaborarHuawei(self):
        self.marca = 'Huawei'

telefono = FabricaTelefonos()
print(telefono.marca)

telefono.elaborarHuawei()
print(telefono.marca)

#El metodo init sirve para crear el constructor de una clase
class FabricaCarros():
    def __init__(self, marca, color):
        print('Estoy ejecutando el metodo Init, porque se ha creado un nuevo objeto')
        self.marca = marca
        self.color = color

carro = FabricaCarros('Toyota', 'Negro')

print(carro.marca)
print(carro.color)



