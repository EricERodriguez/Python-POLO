
class Perro:

    especie = "Canis lupus familiaris"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self, sonido):
        return f"{self.nombre} hace este sonido: {sonido}"

    def __str__(self):
        return f"{self.nombre}tiene {self.edad} edad"
