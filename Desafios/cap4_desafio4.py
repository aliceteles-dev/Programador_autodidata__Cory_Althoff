#4. Escreva um programa com duas funções. A primeira função deve receber um inteiro como
#parâmetro e retornar o resultado do inteiro dividido por 2. A segunda função deve receber um
#inteiro como parâmetro e retornar o resultado do inteiro multiplicado por 4. Chame a primeira
#função, salve o resultado como uma variável e passe-a como parâmetro para a segunda função.
def f1(int):
    return int/2
f1result = f1(4)

def f2(int):
    return int * 4
f2(f1result)

print(f1result)
print(f2(f1result))
