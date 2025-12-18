%%writefile calculadora_geometrica.py
from math import pi

def area_retangulo(l, a):
    return l*a

def perimetro_retangulo(l, a):
    return 2*(l+a)

def area_circulo(r):
    pi * r**2
    
def circunferencia(r):
    return 2 * pi * r

def volume_cubo(l):
    return l**2
