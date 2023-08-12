INSERT INTO prefeitos
	(nome,cidade_id)
Values
	('Rodrigo Neves', 1),
    ('Rafael Nunes', 2),
    ('Brunno Barreto',  null);
    
select * from prefeitos;

INSERT INTO prefeitos
	(nome,cidade_id)
VALUES
	('Jairo Delamare', null) -- Nesse caso não existem problemas já que é nulo, não dará 
							 -- Erro de chave primária