frase1 = input()
frase2 = input()

a = set(frase1.split())
b = set(frase2.split())

common_words = a.intersection(b)
for i in sorted(common_words):
    pass

print(" ".join(sorted(common_words, key=lambda x: (x == "?", x))))