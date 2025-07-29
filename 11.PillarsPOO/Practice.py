#1:
class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def nota(self):
        return self._nota
    
    def resultado(self):
        _resultado = ''
        if self._nota >= 70:
            _resultado = 'Aprobado'
        else:
            _resultado = 'Reprobado'
        print('La nota de {} es de {} y se encuentra {}'.format(self._nombre, self._nota, _resultado))

estudiante = Estudiante('Carlos', 90)

estudiante.resultado()

#2:
class Calculadora():
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
    
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self, numero1):
        self._numero1 = numero1

    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self, numero2):
        self._numero2 = numero2
    
    def calculos(self):
        suma = self._numero1 + self._numero2
        resta = self._numero1 - self._numero2
        multiplicacion = self._numero1 * self._numero2
        division = self._numero1 / self._numero2

        print('suma: {}, resta: {}, multiplicacion: {}, division: {}'.format(suma, resta, multiplicacion, division))

numero1 = float(input("Ingrese el numero 1: "))
numero2 = float(input('Ingrese el numero 2: '))

calculadora = Calculadora(numero1, numero2)

calculadora.calculos()

#3:
class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    @property
    def llantas(self):
        return self._llantas

    @property
    def color(self):
        return self._color

    @property
    def precio(self):
        return self._precio

class Moto(Fabrica):
    pass

class Carro(Fabrica):
    pass

carro = Carro(4, 'Negro', 4200)

print('El carro es de {}, con {} llantas y vale {}'.format(carro.color, carro.llantas, carro.precio))

moto = Moto(2, 'Plateada', 2300)

print('La moto es de {}, con {} llantas y vale {}'.format(moto.color, moto.llantas, moto.precio))

#4:
class Marino():
    def hablar(self):
        print('Hola...')

class Pulpo(Marino):
    def hablar(self):
        print('Soy un pulpo')

class Foca(Marino):
    def __init__(self, mensaje):
        self._mensaje = mensaje
    
    @property
    def mensaje(self):
        return self._mensaje
    
pulpo = Pulpo()

pulpo.hablar()
foca = Foca('Hola')
print(foca.mensaje)

#5:
class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera(Universidad):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

class Estudiante(Carrera):
    def __init__(self, nombre, especialidad, nombreEstudiante, edad):
        super().__init__(nombre, especialidad)
        self.nombreEstudiante = nombreEstudiante
        self.edad = edad

persona = Estudiante('UNED', 'Ingenieria','Carlos', 30)

print(persona.nombre, persona.especialidad, persona.nombreEstudiante, persona.edad)

#6:
class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombre, especialidad, nombreEstudiante, edad):
        Universidad.__init__(self, nombre)
        Carrera.__init__(self, especialidad)
        self.nombreEstudiante = nombreEstudiante
        self.edad = edad

persona = Estudiante('UNED', 'Ingenieria','Carlos', 30)

print(persona.nombre, persona.especialidad, persona.nombreEstudiante, persona.edad)