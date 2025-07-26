class FabricaTelefonos():
    marca = 'Huawei'
    color = 'Negro'
    memoriaRam = 32
    almacenamiento = 128

    #Metodo de intancia, los metodos de instancia siempre tiene el parametro self, son los metodos creados dentro de una clase
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print('Estas escuchando musica')

telefono = FabricaTelefonos()
print(telefono)

telefono.marca
print(telefono.marca)

print(telefono.llamar('Hola, con quien hablo?'))

telefono.escucharMusica()