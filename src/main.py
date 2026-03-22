from gerenciador_eventos import GerenciadorEventos


def exibir_menu():
    print("\n=== UNIEVENTO - SISTEMA DE GERENCIAMENTO DE EVENTOS ===")
    print("1. Cadastrar evento")
    print("2. Listar eventos")
    print("3. Consultar evento por ID")
    print("4. Atualizar evento")
    print("5. Remover evento")
    print("0. Sair")


def cadastrar(gerenciador):
    try:
        id = int(input("ID do evento: "))
        nome = input("Nome do evento: ")
        data = input("Data do evento (AAAA-MM-DD): ")
        local = input("Local do evento: ")
        descricao = input("Descrição do evento: ")
        modalidade = input("Modalidade (presencial/online): ")
        tipo_evento = input("Tipo do evento (palestra, workshop, minicurso...): ")

        gerenciador.cadastrar_evento(id, nome, data, local, descricao, modalidade, tipo_evento)
        print("Evento cadastrado com sucesso.")

    except ValueError as erro:
        print(f"Erro: {erro}")


def listar(gerenciador):
    eventos = gerenciador.listar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    print("\n=== LISTA DE EVENTOS ===")
    for evento in eventos:
        print(evento)


def consultar(gerenciador):
    try:
        id = int(input("Informe o ID do evento: "))
        evento = gerenciador.consultar_evento_por_id(id)

        if evento is None:
            print("Evento não encontrado.")
        else:
            print("\n=== EVENTO ENCONTRADO ===")
            print(evento)

    except ValueError:
        print("Erro: informe um ID válido.")


def atualizar(gerenciador):
    try:
        id = int(input("ID do evento que será atualizado: "))
        nome = input("Novo nome do evento: ")
        data = input("Nova data do evento (AAAA-MM-DD): ")
        local = input("Novo local do evento: ")
        descricao = input("Nova descrição do evento: ")
        modalidade = input("Nova modalidade (presencial/online): ")
        tipo_evento = input("Novo tipo do evento: ")

        gerenciador.atualizar_evento(id, nome, data, local, descricao, modalidade, tipo_evento)
        print("Evento atualizado com sucesso.")

    except ValueError as erro:
        print(f"Erro: {erro}")


def remover(gerenciador):
    try:
        id = int(input("ID do evento que será removido: "))
        gerenciador.remover_evento(id)
        print("Evento removido com sucesso.")

    except ValueError as erro:
        print(f"Erro: {erro}")


def main():
    gerenciador = GerenciadorEventos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar(gerenciador)
        elif opcao == "2":
            listar(gerenciador)
        elif opcao == "3":
            consultar(gerenciador)
        elif opcao == "4":
            atualizar(gerenciador)
        elif opcao == "5":
            remover(gerenciador)
        elif opcao == "0":
            print("Encerrando o sistema UniEvento.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()