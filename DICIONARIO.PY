#

matricula1 = 2026001
nome1 = "Ana Silva"
telefone1 = "9999-8888"

#com dicionario
aluno = {
    "matricula": 2026001,
    "nome": "Ana silva",
    "telefone": "9999-8888" 
}

print(aluno)

contato = {
    "@camila": "camila",
    "@paola":  "paola",
    "@sheron": "sheron",
    "@bruna": "bruna"
    "@joao": "joao"
}

print(contato)
print(type(contato)) 

#acesso direto ao dicionário
print(contato["@camila"])

#acesso seguro com get()
print(contato.get("@paola"))
print(contato.get("inexistente"))
print(contato.get("inexistente", "não encontrado"))

print("original: ", contato) #acessando a lista original

#add novo elemento
contato["@giovanna"] = "giovanna"
print("após add: ", contato)

#atualize elemento existente
contato["@paola"] = "paola oliveira"
print("após add: ", contato)

contato.update({
        "@bruna": "bruna marquezine",
        "@camila": "camila q." 
    })

print("após atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@sheron")

print(f"removildo: {removido}")
print("após o del", contato)

#del remove sem retornar 
del contato["@paola"]
print("após o del; ", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print(" após clear; ", contato)
print("cópia: ", copia)

print("múmero de contato: ", len(contato))

contato.pop("@camila")
print("após remover um: ", len(contato))

#verificar existências
if "@joao" in contato:
    print(f"encontrado: {contato[@joao]}")
#dicionario vazio
vazio = {}

#dicionario com tipos mistos
dados = {
    "nome": "joão",
    "idade": 25,
    "altura": 1.70,
    "ative": True
}

print

("vazio: ", vazio)
print("vazio: ", dados)