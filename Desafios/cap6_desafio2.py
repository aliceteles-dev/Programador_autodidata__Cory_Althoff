#escreva um programa que colete duas strings com um usuário, insira-as na string "Ontem eu escrevi um(a) [resposta_um]. E enviei para [resposta_dois]!" e exiba uma nova string.
texto = input("O que você escreveu? ")
pessoa = input("Para quem você enviou? ")
print("Ontem eu escrevi um(a) {}. E enviei para {}!".format(texto, pessoa))
