from Clase import *
from math import pi

class Figura:
    def __init__(self, p1, p2):
        self.origen = p1
        self.fin = p2
        self.area=0
        self.perimetro =0


class Cuadrado(Figura):
    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.fin)
        #area = lado *lado
        self.area = lado * lado
        #return area
    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro = (lado + lado)*2

class Circulo(Figura):
    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = pi*(radio**2)
        #return area
    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = (2*pi)* radio
        
class Triangulo(Figura):
    def calcular_area(self):
        p3 = Punto(self.origen.x, self.fin.y)
        a_lado = self.origen.calcular_distancia(p3)
        b_lado = p3.calcular_distancia(self.fin)
        self.area = (a_lado * b_lado)/2
      #  self.oringe.x self,origen.y
    def calcular_perimetro(self):
        p3 = Punto(self.origen.x, self.fin.y)
        a_lado = self.origen.calcular_distancia(p3)
        b_lado = p3.calcular_distancia(self.fin)
        c_lado = sqrt((a_lado**2)+(b_lado**2))
        self.perimetro = a_lado + b_lado + c_lado
