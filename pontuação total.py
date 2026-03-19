# 4. Pontuação total
def pontuacao_total(pontos, tempo):
    if tempo < 30:
        pontos = pontos + 50
    elif tempo > 100:
        pontos = pontos - 20

    if pontos > 200:
        return "Recorde"
    else:
        return pontos
