# UniEvento-Sistema-de-Gerenciamento-de-Eventos
Este projeto apresenta o UniEvento, um sistema de gerenciamento de eventos acadêmicos desenvolvido com foco em organização, simplicidade e usabilidade


## 1º parte


## Estrutura das Tabelas

O banco de dados do sistema **UniEvento** foi modelado com as seguintes tabelas principais:

- **usuarios**: armazena os dados dos usuários do sistema, possibilitando o cadastro de participantes.  
- **eventos**: registra os eventos acadêmicos cadastrados na plataforma, contendo informações como nome, data, local, descrição, modalidade e tipo do evento.  
- **inscricoes**: representa a relação entre usuários e eventos, armazenando as inscrições realizadas.

As tabelas foram definidas com:
- **Chaves primárias (PK)** para identificação única dos registros;
- **Chaves estrangeiras (FK)** para manter a integridade entre as tabelas;
- **Restrições como NOT NULL e UNIQUE** para garantir consistência;
- **Tipos de dados adequados** para cada informação, como `VARCHAR`, `INT`, `DATE` e `DATETIME`.

---

## TABELA USUARIOS

| Atributo | Tipo de Dado | Chave | Índice | Restrição |
|---------|-------------|------|--------|----------|
| id | INT | PK | ✔ | NOT NULL, AUTO_INCREMENT |
| nome | VARCHAR(100) |  |  | NOT NULL |
| email | VARCHAR(150) |  | ✔ | NOT NULL, UNIQUE |

---

## TABELA EVENTOS

| Atributo | Tipo de Dado | Chave | Índice | Restrição |
|---------|-------------|------|--------|----------|
| id | INT | PK | ✔ | NOT NULL, AUTO_INCREMENT |
| nome | VARCHAR(150) |  | ✔ | NOT NULL |
| data_evento | DATE |  | ✔ | NOT NULL |
| local_evento | VARCHAR(150) |  |  | NOT NULL |
| descricao | TEXT |  |  | NOT NULL |
| modalidade | VARCHAR(20) |  |  | NOT NULL |
| tipo_evento | VARCHAR(100) |  |  | NOT NULL |

---

## TABELA INSCRICOES

| Atributo | Tipo de Dado | Chave | Índice | Restrição |
|---------|-------------|------|--------|----------|
| id | INT | PK | ✔ | NOT NULL, AUTO_INCREMENT |
| usuario_id | INT | FK | ✔ | NOT NULL |
| evento_id | INT | FK | ✔ | NOT NULL |
| data_inscricao | DATETIME |  |  | DEFAULT CURRENT_TIMESTAMP |

---

## Modelagem SQL para Prototipar o Modelo Físico

Foi desenvolvido o script SQL responsável pela criação das tabelas, seus atributos e relacionamentos, permitindo posteriormente a geração do modelo físico do banco de dados do sistema **UniEvento**.

```sql
DROP DATABASE IF EXISTS unievento;

CREATE DATABASE unievento;
USE unievento;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    data_evento DATE NOT NULL,
    local_evento VARCHAR(150) NOT NULL,
    descricao TEXT NOT NULL,
    modalidade VARCHAR(20) NOT NULL,
    tipo_evento VARCHAR(100) NOT NULL
);

CREATE TABLE inscricoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    evento_id INT NOT NULL,
    data_inscricao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (evento_id) REFERENCES eventos(id)
);

CREATE INDEX idx_eventos_nome ON eventos(nome);
CREATE INDEX idx_eventos_data ON eventos(data_evento);
