nome = input("Digite seu nome")
senha_correta = "123456"

tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha")

    if senha == senha_correta:
        print("Olá,", nome + ". Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas += 1

        if tentativas == 1:
            print("A Senha está incorreta! Você ainda tem 2 tentativas")
        elif tentativas == 2:
            print("A Senha está incorreta! Você ainda tem 1 tentativa")
        else:
            print("A Sua senha foi bloqueada! Por favor, vá até em um dos nossos caixas eletrônicos")