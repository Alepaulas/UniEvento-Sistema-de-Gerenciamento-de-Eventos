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