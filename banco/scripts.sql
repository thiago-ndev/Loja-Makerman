
create database loja;

CREATE TABLE produto(
  id     serial         primary key,
  nome       varchar(50)    not null,
  preco      float          not null);


create table estoque(
    id  serial  primary key,
    produto_nome  varchar,
    constraint fk_nome_produto
    foreign key(produto_nome) references produto(nome)
);


create table endereco(
        id     int      primary key,
        cidade     varchar(30)      not null,
        bairro      varchar(30)     not null,
        rua         varchar(80)     not null,
        numero      varchar(80)     not null
);

CREATE TABLE cliente(
  id     serial     primary key,
  nome       varchar(50)    not null,
  email      varchar(100)  unique not null,
  senha    varchar(255)       not null,
  id_endereco   serial,
  constraint fk_id_endereco
  foreign key(id_endereco) references endereco(id)
);


create table cliente_fisico(
    cpf    varchar(11)      primary key,
    data_Nasc    date  not null
) inherits (cliente);


create table cliente_juridico(
        cnpj    varchar(25)      unique not null,
        ramo     varchar(25)   not null,
        id_cliente    integer  primary key,
        constraint   fk__id_cliente_juridico
        foreign key(id_cliente) references cliente(id)
);

CREATE TABLE cliente(
  id     serial     primary key,
  nome       varchar(50)    not null,
  email      varchar(100)  unique not null,
  senha    varchar(255)       not null,
  type      varchar(20)     not null,
  id_endereco   serial,
   constraint fk_id_endereco
   foreign key(id_endereco) references endereco(id)
);

foreign key(id_endereco) references endereco(id)

create table cliente_fisico(
    id      serial,
    cpf    varchar(15)      unique not null,
    dataNasc    varchar(15)   not null,
    constraint   fk__id_cliente_fisico
    foreign key(id) references cliente(id)
);

alter table cliente_fisico
add column id   ,
constraint   fk__id_cliente_fisico
foreign key(id) references cliente(id);

create table cliente_juridico(
        id     serial           primary key,
        nome    varchar(80)     not null,
        email   varchar(80)    unique not null,
        senha   varchar(255)    not null,
        cnpj    varchar(15)      unique not null,
        ramo     varchar(15)   not null,
        foreign key(id_endereco) references endereco(id)
)
update cliente set id serial primary key;

create table comprar_produto(

);


alter table endereco add column id_cliente  int,
 add constraint fk_id_cliente
 foreign key(id_cliente)
 references cliente(id);
);


alter table endereco
drop column id_cliente;


drop table endereco cascade;

\d produto

SELECT * FROM Produto;

SELECT * FROM Produto limit 3;

SELECT * FROM  produto order by preco;
SELECT * FROM  produto order by id desc;

DELETE FROM produto where id = 4;

UPDATE Produto set nome = 'uva' WHERE id = 8;

