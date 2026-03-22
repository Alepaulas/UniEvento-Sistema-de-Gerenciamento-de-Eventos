from evento import Evento


class GerenciadorEventos:
    def __init__(self):
        self.__eventos = []

    def cadastrar_evento(self, id, nome, data, local, descricao, modalidade, tipo_evento):
        if self.consultar_evento_por_id(id) is not None:
            raise ValueError("Já existe um evento cadastrado com esse ID.")

        novo_evento = Evento(id, nome, data, local, descricao, modalidade, tipo_evento)
        self.__eventos.append(novo_evento)

    def listar_eventos(self):
        return self.__eventos

    def consultar_evento_por_id(self, id):
        for evento in self.__eventos:
            if evento.get_id() == id:
                return evento
        return None

    def atualizar_evento(self, id, nome, data, local, descricao, modalidade, tipo_evento):
        evento = self.consultar_evento_por_id(id)

        if evento is None:
            raise ValueError("Evento não encontrado.")

        evento.set_nome(nome)
        evento.set_data(data)
        evento.set_local(local)
        evento.set_descricao(descricao)
        evento.set_modalidade(modalidade)
        evento.set_tipo_evento(tipo_evento)

    def remover_evento(self, id):
        evento = self.consultar_evento_por_id(id)

        if evento is None:
            raise ValueError("Evento não encontrado.")

        self.__eventos.remove(evento)