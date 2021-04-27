class Rectangulo:

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        return f"{self.ancho*self.longitud}"

    def __str__(self):
        return f"{self.area}"