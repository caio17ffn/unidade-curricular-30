# lendo os valores
Pão = int(input())
Doce = int(input())
Bolo = int(input())

# calculando os pontos
pontos = Pão * 1 + Doce * 2 + Bolo * 3

# verificando o prêmio
if pontos >= 175:
    print("Ganha bolo se os pontos for maior que 175")
elif pontos >= 200:
    print("Ganha doce se os pontos for maior que 200")
elif pontos >= 195:
    print("Ganha pão se os pontos for maior que 195")
else:
    print("Quem vencer ganha o prêmio")