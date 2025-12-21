#the hangman

import random

words = ["carro", "motocicleta", "futebol", "carnaval", "musica", "geografia", "aerosol", "cafune", "bicicleta", "paralelepipedo", "dengo", "amor", "esporte", "mascara", "abacaxi", "avatar", "inacreditavel", "cacto", "sorte", "rosa", "verde", "musgo", "amarelo", "azul", "democracia", "enxada", "trabalho", "livro", "preto", "melancia"]
word = random.choice(words)

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Bem-vindo ao jogo de Forca! \n Regras: \n 1) Se a palavra contiver letras repetidas, você terá que adivinhar a mesma letra mais de uma vez; \n 2) O programa não lê acentos, portanto, ao adivinhar uma letra, escreva-a sem acentuação independente da grafia da palavra. \n Boa sorte!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Adivinhe uma letra "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '@'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("Você venceu!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("Você perdeu! A palavra era {}."
              .format(word))
        
hangman(word)
