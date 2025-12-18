lista = list()
f = open("passaro_mecanico.txt", "r")
lista.append(f.read())
f.close()

print(lista)
