def calcular_total():
    try:
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco2 = float(input("Digite o preço do segundo produto: "))
    except:
        print("Erro: os preços devem ser números!")
        return

    total = preco1 + preco2
    print(f"Total da compra: R$ {total:.2f}")