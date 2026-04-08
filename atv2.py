N = int(input())
R = int(input())
P = int(input())

total = N
novos = N
dias = 0

while total < P:
    novos = novos * R
    total = total + novos
    dias = dias + 1

print(dias)