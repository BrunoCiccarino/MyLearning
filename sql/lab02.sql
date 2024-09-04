DROP DATABASE IF EXISTS cadastro;
CREATE DATABASE cadastro;

CREATE TABLE contato_1nf (
	_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    emails VARCHAR(255)
);
INSERT INTO contato (nome, emails) VALUES
('João', 'joao@pudim.com.br, joao@bol.com.br, joao@ig.com.br'),
('Maria', 'maria@maria.com.br, maria@gmail.com');

