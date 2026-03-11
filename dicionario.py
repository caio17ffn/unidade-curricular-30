# Dicionário com instagram e nome
contato = {
    "@camila": "Camila",
    "paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "João"
}

# Obter chaves
print("Chaves:")
for insta in contato.keys():
    print(insta)

# Obter valores
print("\nValores:")
for nome in contato.values():
    print(nome)

# Obter pares (chave e valor)
print("\nPares:")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")


# Dicionário com instagram e altura
contato = {
    "@camila": 1.66,
    "paola": 1.50,
    "@sheron": 1.80,
    "@bruna": 1.60,
    "@joao": 1.70
}

# Ordenar por chaves
print("\nOrdenado por chaves:")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f} m")


# Ordenar por valor (altura)
from operator import itemgetter

print("\nOrdenado por valor (altura):")
for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{insta} --> {estatura:.2f} m")