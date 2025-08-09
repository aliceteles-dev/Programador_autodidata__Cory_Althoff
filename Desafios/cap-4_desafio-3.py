#3. Escreva uma função que receba três parâmetros obrigatórios e dois parâmetros opcionais.
def f(x, y, z, a=2, b=7):
    return x * y * z / a - b
print(f(2, 3, 4))
