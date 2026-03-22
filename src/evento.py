class Evento:
    def __init__(self, id, nome, data, local, descricao, modalidade, tipo_evento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_data(data)
        self.set_local(local)
        self.set_descricao(descricao)
        self.set_modalidade(modalidade)
        self.set_tipo_evento(tipo_evento)

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_data(self):
        return self.__data

    def get_local(self):
        return self.__local

    def get_descricao(self):
        return self.__descricao

    def get_modalidade(self):
        return self.__modalidade

    def get_tipo_evento(self):
        return self.__tipo_evento

    # Setters com validação
    def set_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    def set_nome(self, nome):
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        self.__nome = nome.strip()

    def set_data(self, data):
        if not isinstance(data, str) or len(data.strip()) == 0:
            raise ValueError("A data do evento é obrigatória.")
        self.__data = data.strip()

    def set_local(self, local):
        if not isinstance(local, str) or len(local.strip()) < 3:
            raise ValueError("O local deve ter pelo menos 3 caracteres.")
        self.__local = local.strip()

    def set_descricao(self, descricao):
        if not isinstance(descricao, str) or len(descricao.strip()) < 5:
            raise ValueError("A descrição deve ter pelo menos 5 caracteres.")
        self.__descricao = descricao.strip()

    def set_modalidade(self, modalidade):
        modalidades_validas = ["presencial", "online"]
        if not isinstance(modalidade, str) or modalidade.strip().lower() not in modalidades_validas:
            raise ValueError("A modalidade deve ser 'presencial' ou 'online'.")
        self.__modalidade = modalidade.strip().lower()

    def set_tipo_evento(self, tipo_evento):
        if not isinstance(tipo_evento, str) or len(tipo_evento.strip()) < 3:
            raise ValueError("O tipo do evento deve ter pelo menos 3 caracteres.")
        self.__tipo_evento = tipo_evento.strip()

    def __str__(self):
        return (
            f"ID: {self.get_id()} | "
            f"Nome: {self.get_nome()} | "
            f"Data: {self.get_data()} | "
            f"Local: {self.get_local()} | "
            f"Modalidade: {self.get_modalidade()} | "
            f"Tipo: {self.get_tipo_evento()} | "
            f"Descrição: {self.get_descricao()}"
        )