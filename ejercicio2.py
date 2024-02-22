class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
    
    def comer(self):
        return "Estoy comiendo"


class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    
    def correr(self):
        return "Estoy corriendo"


class Aguila(Animal):
    def volar(self):
        return "Estoy volando"


