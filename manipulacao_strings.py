#ao lidar com iteráveis, a busca por índice pode ser realizada da esquerda pra direita começando em
#zero ou de trás pra frente, começando em -1 para buscar o último item, -2 pro penúltimo e assim por diante
idades = [29, 21, 40, 32, 57, 19]
print(idades[0])
print(idades[4])
print(idades[-1])
print(idades[-6])
#strings são imutáveis. cada item dentro de uma string tem um índice, e uma string é um elemento iterável,
#porém, se tentar alterar um índice de uma string, sairá a mensagem de erro TypeError: 'str' object does not support item assignment
minha_string = "sou imutável"
print(minha_string[5])

#concatenação de strings
string1 = "cachorro"
string2 = "quente"
print(string1 + string2)

#multiplicação de strings: o conceito me causou estranheza, mas dá pra operar com strings
weird_str = "Oi, você vai me ler cinco vezes!"
print(weird_str * 5)
print("outra string aqui " * 3)

#transformando minúsculas em maiúsculas
print("ngaaaaaaah".upper())

#transformando maiúsculas em minúsculas
print("YOU'RE A WIMPY LOSER WITH A BIG HEART!".lower())

#
print("oi, eu tenho 25 anos!".capitalize())

#format: é útil pra trabalhar com inputs de usuário. Vide o repositório sobre preenchimento automático de documentos digitais. Esse método procura ocorrências de chaves numa string e as
#substitui pelo parâmetro passado

#split
print("Oi! Eu tenho 25 anos!".split("!"))

#join: método que adiciona um caractere entre cada caracter de uma string; permite transformar uma lista de strings em uma única string, usando join() numa string vazia
#(ou com espaços, vírgulas, etc) e passando a lista como parâmetro
vogais = ["a", "e", "i", "o", "u"]
print(", ".join(vogais))

#strip: útil para remover espaços vazios no início ou final de uma string.
oi = "                             Olá!                                           "
print(oi)
print(oi.strip())

#substituicao de caracteres
jam = "Silksong is a really great game"
jam = jam.replace("a", "@")
print(jam)

#o método index busca a primeira ocorrência de um caracter dentro de uma string
print("cachorro-quente".index("-"))
try:
    "animals".index("z")
except:
    print("Not found")

#in ou not in: métodos que retornam valores booleanos e são úteis para verificar se uma string existe ou não existe dentro de outra string
print("jam" in "game jam")
print("video" not in "games")

#escape de string
print("\"Surely!\", she said.")

#linha nova: \n
print("linha1\nlinha2\nlinha3\nlinha4")

#fatiamento
citacao = ["It's a beautiful day outside", "Birds are singing, flowers are blooming.", "On days like this, kids like you", "should be burning in Hell"]
frase1 = citacao[0:1]
frases1_e2 = citacao[0:2]
frases3_e4 = citacao[2:4]
original = citacao[:] #se o índice inicial for 0, pode deixar vazio; se o final for o último do iterável, também pode ficar vazio; deixar ambos vazios retorna o iterável inteiro.
print(frase1)
print(frases1_e2)
print(frases3_e4)
print(original)
