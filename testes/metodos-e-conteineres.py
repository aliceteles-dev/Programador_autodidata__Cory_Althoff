#lista == contêiner que armazena objetos em uma ordem específica
cores = ["roxo", "azul", "amarelo"]
cores.append("lilás")

def jogo_adivinhacao():
    adivinhe = input("Adivinhe em que cor estou pensando agora: ")
    if adivinhe in cores:
        print("Você acertou!")
    else:
        print("Tente novamente ")
        jogo_adivinhacao()

jogo_adivinhacao()
