select * from estados

insert into cidades 
	(nome, estado_id, area)
VALUES
	('São Paulo',50, 11.2)
    
INSERT INTO cidades (nome, estado_id, area)
VALUES ('Niterói', 25, 133.9)


INSERT INTO cidades(nome, estado_id, area)
VALUES('Caruaru', (select id from estados where sigla = 'PE'), 920.6)

INSERT INTO cidades(nome, estado_id, area)
VALUES('Campo Grande', (select id from estados where sigla = 'MS'), 1000.5)



select * from cidades