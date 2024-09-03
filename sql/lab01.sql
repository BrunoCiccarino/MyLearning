drop database if exists loja;
create database loja;

create table loja.cliente(
	_id int auto_increment primary key,
	nome varchar(100),
	email varchar(100)
);

insert into loja.cliente(
	nome,
	email
)
values(
	'Bruno',
	'bruno@gmail.com'
), (
	'João',
	'joao@gmail.com'
), (
	'Maria',
	'maria123@gmail.com'
);

select * from loja.cliente;

update loja.cliente
	set email = 'brunoc@gmail.com'
	where _id = 1;


select * from loja.cliente; 	
alter table loja.cliente add column numero varchar(20) unique;

insert into loja.cliente(
	numero
) value (
	'+5541987786862'
), (
	'+554199003224'
), (
	'+5541988443074'
);

create table loja.venda(
	_id int auto_increment primary key,
    cliente_id int,
    dt_venda date,
    valor_total decimal(6,2) not null
);

insert into loja.venda(
    cliente_id,
    dt_venda,
    valor_total
) value(
	1,
    '2022-09-27',
    275.00
), (
	1,
    '2024-08-23',
    556.09
), (
	1,
    '2024-04-23',
    336.88
);

select * from loja.venda where valor_total > 100;

alter table loja.venda add column estado enum('Pendente', 'Pago', 'Cancelado');

update loja.venda
	set estado = 'Pendente'
	where _id = 1;
    
update loja.venda
	set estado = 'Pago'
	where _id = 2;
update loja.venda
	set estado = 'Cancelado'
	where _id = 3;

select estado from loja.venda where estado = 'Pago';

create table loja.produto(
	_id int auto_increment primary key,
    nome varchar(50),
    preco decimal (5,2)
);

insert into loja.produto(
    nome,
    preco
) value(
	'Banana',
    551.22
), (
	'Maça',
    333.44
), (
	'Pera',
    777.22
);

select * from loja.produto;

update loja.produto
	set preco = preco * 0.2
	where _id = 1;

update loja.produto
	set preco = preco * 0.2
	where _id = 2;

update loja.produto
	set preco = preco * 0.2
	where _id = 3;
    
select * from loja.produto;
