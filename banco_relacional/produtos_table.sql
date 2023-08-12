CREATE TABLE produtos(
	id int unsigned not null AUTO_INCREMENT,
    nome VARCHAR(255) not null,
    valor float not null,
    quantidade int not null,
    PRIMARY KEY(id),
    UNIQUE KEY (nome)
);

insert into produtos(nome,valor,quantidade) 
VALUES
	('Copo de plástico', 10.99, 20),
    ('Tesoura', 4.95, 10),
    ('Celular Moto G20', 700, 1);

insert into produtos(nome,valor, quantidade) values
    ('Carregador', 50, 5),
    ('Fone de ouvido', 35, 10);
    
    
select * from produtos