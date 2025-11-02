'''6. Escreva um programa com uma variável age que receba um inteiro e exiba strings diferentes
dependendo de que inteiro age receber'''
age = 17
if age <= 15:
    print("Você ainda não tem idade para votar.")
elif age < 18 or age >= 70:
    print("Você pode votar, mas não é obrigado!")
else:
    print("Você deve votar!")
