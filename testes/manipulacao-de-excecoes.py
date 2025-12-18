def continha():
    a = input("Digite um número: ")
    b = input("Digite outro: ")
    a = int(a)
    b = int(b)
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Digite apenas números, sendo que b deve ser diferente de 0")
        continha()

continha()
    
