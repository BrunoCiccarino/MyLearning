DROP DATABASE IF EXISTS aula;
CREATE DATABASE aula;
USE aula;

CREATE TABLE produto (
	_id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    valor_unitario DECIMAL(8, 2) NOT NULL,
    estoque INT,
    departamento VARCHAR(50) NOT NULL
);

CREATE TABLE venda (
	_id SERIAL PRIMARY KEY,
    produto_fk BIGINT UNSIGNED NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (produto_fk) REFERENCES produto(_id)
);

INSERT INTO produto (nome, valor_unitario, estoque, departamento)
VALUES
('Camisa', 24.49, 50, 'Vestuário'),
('Camiseta', 38.88, 30, 'Vestuário'),
('Tênis', 88.77, 20, 'Calçados'),
('Camisola', 29.97, 15, 'Vestuário'),
('Chinelo', 14.47, NULL, 'Calçados');

INSERT INTO venda (produto_fk, quantidade) VALUES
(1, 5), (2, 3), (3, 2), (1, 7), (4, 6);

SELECT SUM(quantidade) AS total_vendido FROM venda;

SELECT v.quantidade * p.valor_unitario AS valor_total
FROM venda v
JOIN produto p ON v.produto_fk = p._id;

SELECT AVG(v.quantidade * p.valor_unitario) AS media_das_vendas
FROM venda v
JOIN produto p ON v.produto_fk = p._id;

SELECT MAX(v.quantidade * p.valor_unitario) AS venda_mais_cara
FROM venda v
JOIN produto p ON v.produto_fk = p._id;

SELECT MIN(v.quantidade * p.valor_unitario) AS venda_mais_barata
FROM venda v
JOIN produto p ON v.produto_fk = p._id;

SELECT COUNT(*) AS numero_de_vendas FROM venda;

SELECT ROUND(AVG(v.quantidade * p.valor_unitario), 2) AS media_das_vendas
FROM venda v
JOIN produto p ON v.produto_fk = p._id;

SELECT TRUNCATE(AVG(v.quantidade * p.valor_unitario), 2) AS media_das_vendas
FROM venda v
JOIN produto p ON v.produto_fk = p._id;

SELECT nome, RAND() AS numero_aleatorio FROM produto;

SELECT DATE_FORMAT(NOW(), '%d/%m/%Y') AS data_formatada;

SELECT DAYNAME(NOW()) AS dia_da_semana;

SELECT * FROM produto WHERE _id IN (1, 3, 4);

SELECT * FROM produto WHERE valor_unitario BETWEEN 25 AND 40;

SELECT * FROM produto WHERE nome LIKE 'C%';

SELECT * FROM produto WHERE nome LIKE '%ta';

SELECT * FROM produto WHERE nome LIKE '%e%';

SELECT * FROM produto WHERE estoque IS NULL;

SELECT * FROM produto WHERE _id NOT IN (2, 4);

SELECT * FROM produto WHERE valor_unitario NOT BETWEEN 20 AND 30;

SELECT * FROM produto WHERE nome NOT LIKE 'Ca%';

SELECT * FROM produto
ORDER BY valor_unitario ASC;

SELECT * FROM produto
ORDER BY valor_unitario DESC, estoque DESC;

SELECT * FROM produto
WHERE estoque > 20
ORDER BY nome DESC;

SELECT * FROM produto
WHERE valor_unitario > 20
ORDER BY valor_unitario
LIMIT 3;

SELECT * FROM produto
ORDER BY valor_unitario DESC
LIMIT 1
OFFSET 2;

SELECT p.nome, COUNT(v._id) AS total_vendas_do_produto
FROM venda v
RIGHT JOIN produto p ON v.produto_fk = p._id
GROUP BY p._id;

SELECT departamento, COUNT(*) AS total_produtos
FROM produto
GROUP BY departamento
HAVING COUNT(*) > 2;

SELECT departamento, COUNT(*) AS total_produtos
FROM produto
WHERE departamento LIKE 'V%'
GROUP BY departamento
HAVING total_produtos > 2;

SELECT *
FROM produto p
WHERE EXISTS (
	SELECT *
    FROM venda v
    WHERE v.produto_fk = p._id
);

SELECT *
FROM produto p
WHERE NOT EXISTS (
	SELECT *
    FROM venda v
    WHERE v.produto_fk = p._id
)