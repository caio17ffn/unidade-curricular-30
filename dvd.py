def soma_segura(a, b):
    try:
        s = a + b
        return s
    except:
        print("Entrada inválida")
        return 0


def divisao(x, y):
    try:
        d = x / y
        return d
    except:
        return "Não divida por zero!"