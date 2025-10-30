#escreva um programa que permita que o usuário pergunte sua altura, cor favorita ou autor favorito e retorne o resultado a partir do dicionário criado no desafio anterior.

#dicionário:
about_me = {"altura": "1.64",
            "cor_favorita": "roxo",
            "autor_favorito": "Clarice Lispector",
            "primeira_linguagem_de_programação": "GML"
            }

#programa
resposta = input("Digite altura, cor_favorita, autor_favorito ou primeira_linguagem_de_programação: ")
if resposta in about_me:
                 resultado = about_me[resposta]
                 print(resultado)
