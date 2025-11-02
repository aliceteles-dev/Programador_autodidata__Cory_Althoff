lista = [1, 3, 5, 7, 9, 11]

while True:
    guess = input("Adivinhe o número no qual estou pensando, ou digite \"q\" para sair ")
    if guess == "q":
        break
    guess = int(guess)
    if guess in lista:
        print("Parabéns! Você acertou!")
    else:
        print("Tente novamente.")


