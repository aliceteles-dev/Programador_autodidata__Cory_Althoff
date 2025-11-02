#Multiplique todos os números da lista [8, 19, 148, 4] por todos os números da lista [9, 1, 33, 83] e acrescente cada resultado a uma terceira lista

lista1 = [8, 19, 148, 4]
lista2 = [9, 1, 33, 83]
resultado = []

for i in lista1:
    for j in lista2:
        z = (i * j)
        resultado.append(z)

print(resultado)

