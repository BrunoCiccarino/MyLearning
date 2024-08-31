DROP DATABASE IF EXISTS aula_02;
CREATE DATABASE aula_02;

CREATE TABLE aula_02.estudante(
	_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    teste INT
);

ALTER TABLE aula_02.estudante ADD COLUMN dt_nasc DATE;
SELECT * FROM aula_02.estudante;

-- ALTER TABLE aula_02.estudante DROP COLUMN dt_nasc;
ALTER TABLE aula_02.estudante MODIFY COLUMN teste VARCHAR(50);