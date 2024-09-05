DROP DATABASE IF EXISTS Aulas_sql;
CREATE DATABASE Aulas_sql;

USE Aulas_sql;
CREATE TABLE contatos (
	_id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    emails VARCHAR(255)
);

INSERT INTO contatos (nome, emails) VALUES
('joão', 'Joao@gmail.com, joao@pudim.com, joao@uber.com'),
('Roberto', 'roberto@gmail.com, roberto@pudim.com, roberto@uber.com'),
('Matheus', 'matheus@gmail.com, matheus@pudim.com, matheus@uber.com'),
('Bruno', 'bruno@gmail.com, bruno@pudim.com, bruno@uber.com'),
('Maria', 'Maria@gmail.com, maria@pudim.com');

SELECT * FROM contatos;

CREATE TABLE contato_1nf (
	_id SERIAL PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE email (
	_id SERIAL PRIMARY KEY,
	contato_fk BIGINT UNSIGNED,
    email VARCHAR(255) NOT NULL,
    FOREIGN KEY (contato_fk) REFERENCES contato_1nf(_id)
);

INSERT INTO contato_1nf (nome) VALUES
('João'),
('Roberto'),
('Matheus'),
('Bruno'),
('Maria');

INSERT INTO email (contato_fk, email) VALUES 
(1, 'Joao@gmail.com'),
(1, 'joao@pudim.com'),
(1, 'joao@uber.com'),
(2, 'roberto@gmail.com'),
(2, 'roberto@pudim.com'),
(2, 'roberto@uber.com'),
(3, 'matheus@gmail.com'),
(3, 'matheus@pudim.com'),
(3, 'matheus@uber.com'),
(4, 'bruno@gmail.com'),
(4, 'bruno@pudim.com'),
(4, 'bruno@uber.com'),
(5, 'Maria@gmail.com');

SELECT c._id, c.nome, e.email
	FROM contato_1nf AS c
	JOIN email e ON c._id = e.contato_fk;