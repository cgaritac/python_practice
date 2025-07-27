class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print('El objeto {} ha sido creado'.format(self.marca))

    #El metodo str es para modificar la descripcion del objeto
    def __str__(self):
        return 'El objeto es {}'.format(self.marca)
    
    #Metodo destructor para destruir los objetos una vez que se ha finalizado su ejecucion
    def __del__(self):
        print('El objeto {} ha sido destruido'.format(self.marca))


telefono = FabricaTelefonos('Huawei', 'Negro')
print(telefono.marca)
print(telefono)


