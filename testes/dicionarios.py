#dicionários: associação de par chave-valor
rimas_ingles = {"1": "begun",
                "2": "new",
                "3": "me",
                "4": "more",
                "5": "alive"
                }

n = input("Digite um número: ")
if n in rimas_ingles:
    rima = rimas_ingles[n]
    print(rima)
else: print("Não encontrado")


