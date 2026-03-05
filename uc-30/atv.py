import random

# Primeira lista
numeros = [91, 34, 67, 15, 82]

# 1. Mostrar lista original
print("Lista original:", numeros)

# 2. Ordenar em ordem crescente
numeros.sort()
print("Ordem crescente:", numeros)

# 3. Ordenar em ordem decrescente
numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)


# Segunda lista
dados = [80, 7, 10, 9, 19]

# Embaralhar lista
random.shuffle(dados)

print("Lista embaralhada:", dados)


# Desafio - Terceira lista
terceira_lista = [5, 12, 3, 25, 18, 9]

print("\nTerceira lista original:", terceira_lista)

# Ordem crescente
terceira_lista.sort()
print("Terceira lista crescente:", terceira_lista)

# Ordem decrescente
terceira_lista.sort(reverse=True)
print("Terceira lista decrescente:", terceira_lista)

# Embaralhar
random.shuffle(terceira_lista)
print("Terceira lista embaralhada:", terceira_lista)