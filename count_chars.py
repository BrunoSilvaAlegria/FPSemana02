dic = {}
frase = input()
frase = frase.strip()

for i in frase:
    dic[i] = frase.count(i)
    if i == " ":
        del dic[i]

print(dic)