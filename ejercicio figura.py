from figura import *
p1 = Punto (1,5)
p2 = Punto (10,1)
#p3 = Punto (1,5)

cuadrado = Cuadrado(p1, p2)
circulo = Circulo (p1, p2)
triangulo = Triangulo (p1,p2)
cuadrado.calcular_area()
circulo.calcular_area()
triangulo.calcular_area()
print cuadrado.area
print circulo.area
print triangulo.area
print cuadrado.perimetro
print circulo.perimetro
print triangulo.perimetro
#print cuadrado.calcular_area()
#print circulo.calcular_area()
