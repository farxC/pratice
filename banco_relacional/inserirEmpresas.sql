INSERT INTO empresas
	(nome, cnpj)
VALUES
	('Bradesco', 9999100219301),
    ('Vale', 8232392392),
    ('Cielo', 012018218121);

insert into empresas_unidades
	(empresa_id, cidade_id, sede)
VALUES
	(1,1,1),
    (1,2,0),
    (2,1,0);
    
ALTER TABLE empresas modify cnpj VARCHAR(18);
    
DESC empresas; -- Ajuda a descrever a tabela

select * from empresas;
select * from cidades
    