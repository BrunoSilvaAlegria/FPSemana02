dic = {}
frase = input()

for i in frase:
    dic[i] = frase.count(i)

print(dic)