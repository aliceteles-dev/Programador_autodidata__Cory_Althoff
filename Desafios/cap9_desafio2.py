cor = input("Qual é a sua cor favorita?")


with open("fav.txt", "w") as f:
    f.write(cor)
    
