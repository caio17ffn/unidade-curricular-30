num = int(input("Digite um número inteiro positivo: "))

if num % 2 == 0:
    resultado = num ** 2
    print("O número é PAR")
    print("Quadrado =", resultado)
else:
    resultado = num ** 3
    print("O número é ÍMPAR")
    print("Cubo =", resultado)