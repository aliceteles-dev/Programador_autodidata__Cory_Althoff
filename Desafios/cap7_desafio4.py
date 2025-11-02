#escreva um programa com um loop infinito (com a opção de digitar q para sair) e uma lista de números. A cada iteração do loop, peça ao usuário para fornecer um
#número da lista e informe se o seu palpite estava ou não correto.
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


