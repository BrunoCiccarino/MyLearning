DROP DATABASE IF EXISTS primeiro_banco;
CREATE DATABASE primeiro_banco;

/* Tipos de drop
DROP DATABASE primeiro_banco
DROP DATABASE IF EXISTS primeiro_banco;
Apague a db caso exista
*/

CREATE TABLE primeiro_banco.cliente(
	cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    valor DECIMAL(8, 2),
    _data DATE,
    _hora TIME,
    ativo BOOLEAN
);

/**
* Schema é uma estrutura lógica que define a organização de dados dentro de um banco de dados
*/

/* Comandos DDL
ALTER <tipo do objeto> <nome> <ação> <detalhes da ação>
DROP <tipo do objeto> <nome>
RENAME <nome antigo> TO <nome novo>
TRUNCATE TABLE <nome da tabela>
*/

/* Comandos dml
INSERT INTO <tabela> (<colunas>) VALUE (<valores>)
UPDATE <tabela> SET <coluna1> = <valor1>, <coluna2> = <valor2>, ... WHERE <condicao>;
DELETE <nome da tabela> WHERE <condicao> <detalhes>
*/

INSERT INTO primeiro_banco.cliente(
	nome,
    email,
    valor,
    _data,
    _hora,
    ativo
)

VALUES(
	'Bruno',
    'brunociccarino@gmail.com',
    125.15,
    '2024-08-30',
    '20:33:55',
    true
), (
	'Maria',
    'maria@gmail.com',
     -1235.55,
     '2024-09-15',
     '29:55:59',
    false
);

SELECT * FROM primeiro_banco.cliente;
SELECT * FROM primeiro_banco.cliente WHERE ativo = true;
/* Comandos dql
SELECT <colunas> FROM <tabela> WHERE <condição> 
*/

UPDATE primeiro_banco.cliente 
	SET email = 'email@joao.com.br'
	WHERE cliente_id = 1;

SET SQL_SAFE_UPDATES = 0;

/*Tipos de dados numericos
INTEGER numeros inteiros que podem ser SIGNED e UNSIGNED
TINYINT: 1 BYTES, valor minimo assinado: -128 valor minimo não assinado: 0, valor maximo assinado: 127, valor maximo não assinado: 255
SMALLINT: 2 BYTES, valor minimo assinado: -32768, valor minimo não assinado: 0, valor maximo assinado: 32767, valor maximo não assinado: 65535
MEDIUMINT: 3 BYTES,
*/

/* Strings
CHAR(n): sempre vai ter um tamanho fíxo de até n caracteres
VARCHAR(n): vai ter um tamanho variado de caracteres e vai ter o comprimento real da string
*/

/*Textuais
TEXT Não é possível especificar um tamanho fixo e sempre vai ter o comprimento real da string e é armazenado em outro local
TINYTEXT tamano maximo 255 bytes
MEDIUMTEXT tamanho maximo 16.777.215
LONGTEXT tamanho maximo 4.294.967.295
*/