import json

contatos_suportados = ("telefone", "email", "endereco")

#Dicionário de exemplo, com alguns dados padrão
agenda = {
    "Robson": {
        "telefone": ["11 1234-5678"],
        "email": ["robs@email.com", "robsonsilva@profissional.com"],
        "endereco": ["Rua 123"]
    },
    "John Doe": {
        "telefone": ["11 9874-5678"],
        "email": ["johnzera@email.com", "john.d@profissional.com"],
        "endereco": ["Rua 345"]
    }
}

def carrega_agenda_inicial(agendajson="second_steps/m4_agenda.json"):
    try:
        with open(agendajson, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de agenda inicial não encontrado. Nossa agenda está VAZIA!")
        return {}

def contato_para_texto(nome_contato: str, **formas_contato):
    """Recebe um nome de contato com string e um dicionário
    com as formas de contato.
    Retorna uma string com os dados recebidos"""

    formato_texto = f"{nome_contato}"
    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas} - {valor.upper()}"
            contador_formas = contador_formas + 1
    return formato_texto


def agenda_para_texto(**agenda_completa):
    print("Aqui estão seus contatinhos:\n")
    formato_texto=""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto}{contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}------------------------------\n"
    return formato_texto


def altera_nome_contato(agenda_original:dict, nome_original:str, nome_atualizado:str):
    if nome_original in agenda_original.keys():
        copia_contatos = agenda_original[nome_original].copy()
        agenda_original.pop(nome_original)
        agenda_original[nome_atualizado] = copia_contatos
        return True
    return False


def altera_forma_contato(lista_contatos:list, valor_antigo:str, novo_valor:str):
    if valor_antigo in lista_contatos:
        posicao_valor_antigo = lista_contatos.index(valor_antigo)
        lista_contatos.pop(posicao_valor_antigo)
        lista_contatos.insert(posicao_valor_antigo, novo_valor)
        return True
    return False



def exclui_contato(agenda:dict, nome_contato:str):
    if nome_contato in agenda.keys():
        agenda.pop(nome_contato)
        return True
    return False

def inclui_contato(agenda:dict, nome_contato:str, **formas_contato):
    agenda[nome_contato] = formas_contato

def inclui_forma_contato(formas_contato:dict, forma_incluida:str, valor_incluido:str):
    if forma_incluida in formas_contato.keys():
        formas_contato[forma_incluida].append(valor_incluido)
        return True
    elif forma_incluida in contatos_suportados:
        formas_contato[forma_incluida] = [valor_incluido]
        return True
    return False


def usuario_inclui_contato(agenda:dict):
    nome = input("Qual é o nome da pessoa? ")
    dicionario_formas = {}
    for forma in contatos_suportados:
        resposta = input (f"Deseja inserir um {forma} para {nome.upper()}? \n SIM OU NÃO -> ")
        lista_contatos = []
        while "S" in resposta.upper():
            lista_contatos.append(input(f"informe um {forma}: "))
            resposta = input(f"Deseja inserir outro {forma}? \n SIM ou NÃO -> ")
        if len(lista_contatos) > 0:
            dicionario_formas[forma] = lista_contatos.copy()
            lista_contatos.clear()
    if len(dicionario_formas.keys()) > 0:
        inclui_contato(agenda, nome, **dicionario_formas)
        print("Deu tudo certo!!")
    else:
        print("Ops! É necessário incluir pelo menos uma forma de contato... \n A agenda não foi alterada :x ")

def usuario_inclui_forma_contato(agenda:dict):
    nome = input("Qual é o nome do contato que você quer adicionar aos contatinhosssss? ")
    if nome in agenda.keys():
        print(f"As formas de contato suportadas pelo sistema são: {contatos_suportados}")
        forma_incluida = input("Qual forma de contato deseja incluir? ")
        if forma_incluida in contatos_suportados:
            valor_incluido = input(f"Informe o {forma_incluida} que deseja incluir: ")
            if inclui_forma_contato(agenda[nome], forma_incluida, valor_incluido):
                print("Sucesso!!")
            else:
                print("Alguma coisa deu errado, sorry...")
        else:
            print("Não conheço esta forma de contato")
    else:
        print("Opa, este contato não existe!")

def usuario_exclui_contato(agenda:dict):
    nome = input("Qual é o nome de quem vai ir de base?! ")
    if exclui_contato(agenda, nome):
        print("Pronto, tá excluído!")
    else:
        print("Não encontrei ninguém com esse nome...")

def usuario_altera_nome_contato(agenda:dict):
    nome_original = input("Quem você quer alterar? ")
    nome_atualizado = input("Qual é o novo nome? ")
    if altera_nome_contato(agenda, nome_original, nome_atualizado):
        print(f"Contato atualizado, agora o nome dele é {nome_atualizado}!")
    else:
        print(f"Não achei o contato inicial... não consegui mudar o nome de ninguém")

def usuario_altera_forma_contato(agenda:dict):
    nome = input("Quem é o contatinho que vai mudar? ")
    if nome in agenda.keys():
        print(f"As formas de contato são estas: {contatos_suportados}")
        forma_incluida = input("Qual forma de contato deseja incluir?")
        if forma_incluida in contatos_suportados:
            print(contato_para_texto(nome, **agenda[nome]))
            valor_antigo = input(f"Informe o {forma_incluida} que deseja alterar")
            nova_valor = input(f"Informe o novo {forma_incluida} ")
            if altera_forma_contato(agenda[nome][forma_incluida], valor_antigo, nova_valor):
                print("Contato alterado!")
            else:
                print("Ops, algo deu errado!")
        else:
            print(f"{forma_incluida} não é uma forma de contato suportada pelo sistema!")
    else:
        print(f"O contato {nome} não está na agenda :c ")

def usuario_contato_para_texto(agenda:dict):
    nome = input("Informe o nome do contatinho que deseja exibir: ")
    if nome in agenda.keys():
        print(contato_para_texto(nome, **agenda[nome]))
    else:
        print("Epa! Não tem ninguém com esse nome aqui")

#Arquivos externos

def agenda_para_txt(nome_arquivo:str, agenda):
    if "txt" not in nome_arquivo:
        nome_arquivo = f"{nome_arquivo}.txt"
    with open(nome_arquivo, "w", encoding = "utf-8") as arquivo:
        arquivo.write(agenda_para_texto(**agenda))
        print ("Ihu!! Agenda exportada com sucesso!")

def json_para_agenda(nome_arquivo:str):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print("Ihu!! Agenda carregada com sucesso!")
    return json.loads(conteudo)

def agenda_para_json(nome_arquivo:str, agenda):
    if ".json" not in nome_arquivo:
        nome_arquivo = f"{nome_arquivo}.json"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(agenda, indent=4, ensure_ascii=False))
        print("Ihu!! Agenda exportada com sucesso!")

#interface

def manipulador_agenda():
    agenda = carrega_agenda_inicial()
    op = 1
    while op !=12:
        exibe_menu()
        op = int(input("O que deseja fazer? Escolha um número!"))
        if op == 1:
            usuario_inclui_contato(agenda)
        elif op == 2:
            usuario_inclui_forma_contato(agenda)
        elif op == 3:
            usuario_altera_nome_contato(agenda)
        elif op == 4:
            usuario_altera_forma_contato(agenda)
        elif op == 5:
            usuario_contato_para_texto(agenda)
        elif op == 6:
            print(agenda_para_texto(**agenda))
        elif op == 7:
            usuario_exclui_contato(agenda)
        elif op == 8:
            nome_arquivo = input("\nInforme o nome ou caminho do arquivo")
            agenda_para_txt(nome_arquivo, agenda)
        elif op ==9:
            nome_arquivo = input("\nInforme o nome ou caminho do arquivo")
            agenda_para_json(nome_arquivo, agenda)
        elif op ==10:
            nome_arquivo = input("\nInforme o nome ou caminho do arquivo")
            agenda = json_para_agenda(nome_arquivo)
        elif op ==11:
            print("\nSaindo de fininho... tchau!")
            break
        else:
            print("\nOpção inválida, tente novamente!")

def exibe_menu():
    print("\n\n")
    print("\nEu sou sua lista de contatinhos! Veja suas opções:\n")
    print("1 - Incluir contatinho na agenda")
    print("2 - Incluir forma de contato")
    print("3 - Alterar o nome de um contatinho")
    print("4 - Alterar uma forma de contato")
    print("5 - Mostrar um contatinho")
    print("6 - Mostrar toda a agenda")
    print("7 - Excluir contatinho -> ui, cuidado!!")
    print("8 - Exportar agenda em txt")
    print("9 - Exportar agenda em JSON")
    print("10 - Importar agenda JSON")
    print("11 - Sair")
    print("\n")        

manipulador_agenda()