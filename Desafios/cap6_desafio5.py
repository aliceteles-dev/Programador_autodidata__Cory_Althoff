#pegue a lista ["The", "fox", "jumped", "over", "the", "fence", "."] e transforme-a em uma string gramaticalmente correta.
phrase = " ".join(["The", "fox", "jumped", "over", "the", "fence", "."])
print(phrase)

phrase = phrase[0: -2] + "."
print(phrase)
