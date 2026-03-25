def resumo_notas(notas):
    soma = 0

    for n in notas:
        soma = soma + n

    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    return soma, media, maior, menor


# exemplo de uso
lista = [7, 8.5, 6, 9, 10]

soma, media, maior, menor = resumo_notas(lista)

print("Soma:", soma)
print("Média:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)