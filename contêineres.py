#Contêineres em Python servem para armazenar objetos (dados) de forma organizada.
#Listas, tuplas e dicionários são tipos de contêineres.

#As listas armazenam os objetos em uma ordem específica, organizando-os em índices. O primeiro índice sempre é 0.
#Sintaxe: podemos criar uma lista de algumas formas:
# 1) Nome da lista = list( )
# 2) Nome da lista = [ ]  -->  nome da lista = [0, 1, 2, 3...]
'''
execute os exemplos a seguir no shell:
'''
fruit = []
fruit

fruit = ["Apple", "Orange", "Pear"]
fruit

'''
#Para adicionar um novo item à lista, usamos o MÉTODO append:
fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
print(fruit)
#NOTA: o append sempre vai adicionar um novo item ao fim da lista.

#As listas não se limitam a armazenar strings; elas podem armazenar qualquer tipo de dado.
random = []
print(random)
random.append("True")
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

#As strings, as listas e as tuplas são ITERÁVEIS, ou seja, podemos acessar cada item usando um loop. E cada item de um iterável tem um índice.
#Recuperando um item utilizando seu índice:
print(random[3])
#Exceção que pode ocorrer: Out of range.

print(random[7])
Retorno: "IndexError: list index out of range"


# A lista é um contêiner mutável, já que é possível adicionar, alterar ou remover objetos.
# Para alterar um item em uma lista, basta atribuir seu índice a um novo objeto:
colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red"
print(colors)

# pop:
# O pop se trata de um método utilizado para remover o último item de uma lista.
colors.pop()
print(colors)

# Exemplo do livro -- página 79
colors = ["blue", "green", "yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)
'''
'''
# Se tentar utilizar uma lista vazia, o Python vai lançar uma exceção.
frutas = list()
print(frutas)
frutas.pop() # retorno: "IndexError: pop from empty list"
'''
'''
# É possível combinar duas listas com o operador de adição:
colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print(colors1 + colors2)
#retorno: "['blue', 'green', 'yellow', 'orange', 'pink', 'black']"
'''
'''
#Podemos verificar se um item existe em uma lista com a palavra-chave in
colors = ["blue", "green", "yellow"]
print("green" in colors)
 #retorno: True
'''
'''
#Podemos usar a palavra-chave not para verificar se um item NÃO existe em uma lista:
colors = ["blue", "green", "yellow"]
print("black" not in colors)
#retorno: True
print("blue" not in colors)
#retorno: False


# Podemos usar a função len para saber o tamanho de uma lista (o número de itens que existem nela)
print(len(colors))
#retorno: 3
'''

#Usando uma lista na prática: exemplo página 80
colors = ["purple", "orange", "green"]
guess = input("Guess a color: ")
if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again!")






















