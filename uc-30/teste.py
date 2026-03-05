import random

numeros= [45, 12, 78, 23, 56]
print("Lista oficial : " , numeros)

# sort crescente
numeros.sort()
print("Apóssort(): ", numeros)

# sort decrescente
numeros.sort(reverse=True)
print("Apóssort(): ", numeros)  

#embaralhar
dados = [1, 2, 3, 4, 5]
random.shuffle(dados)
print("Embarahar; ", dados)

