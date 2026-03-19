# 2. Sistema bancário
def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    else:
        if saque > 1000:
            taxa = saque * 0.02
            saldo = saldo - saque - taxa
        else:
            saldo = saldo - saque
        return saldo