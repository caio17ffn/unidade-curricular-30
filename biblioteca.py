#SISTEMA DE GESTÃO DE BIBLIOTECA

#Dicionário p/ armazenar os livros
catalogo = {}

#Dicionário p/ armazenar os empréstimos ativos
emprestimosAtivos = {}

#lista p/ armazenar o histórico de transição
historico = {}

# Função: Adicionar livro

def adicionarlivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False

    catalogo [codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarlivro("L001", "Codigo Limpo", "Robert Martin", 2)

#FUNÇÃO: EMPRESTAR LIVRO


def empresta_livro(codigo, nome_aluno):

    #VALIDAÇÃO 1: Livro existe no catálogo?
    if codigo not in catalogo:
        print(f"Erro: Livro com código (codigo) não encontradol")
        return False


    # VALIDAÇÃO 2: Hấ quantidade disponivel?
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: "(catalogo[codigo]['titulo'])" não está disponívell")
        return False


    # VALIDAÇÃO 3: Aluno ja pegou 2 livros?
    livros_do_aluno = conta_ livros_aluno(noma_aluno)
    if livros do_aluno >= 2:
        print(f"Erro: (nome_aluno) já pegou 2 livros (limite máximo)|")
        return False
    
        #VALIDAÇÃO 4: Aluno já pegou este livro?
    if codigo in emprestimoAtivo and nome aluno in emprestimoAtivo[codigo]:
        print(f"Erro: (nome_aluno) já pegou aste livrol")
        return False
    
    if codigo not in emprestimoAtivo:
     emprestimoAtivo[codigo] = []


    Adiciona o aluno à lista de quem pegou este livro
    emprestimoAtivo[codigo].append(nome_aluno)


# Diminui (parameter) codigo: Any
catalogo[codigo]["quantidade"]
1


# Registra no histórico
historico.append()
'tipo": "emprestimo",
"codigo": codigo,
"titulo": catalogo[codigo]["titulo"].