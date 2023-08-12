select * from cidades as c inner join prefeitos as p on c.id = p.cidade_id;

select * from cidades c left join prefeitos p on c.id = p.cidade_id;

select c.nome, p.nome, c.id from cidades c left join prefeitos p on c.id = p.cidade_id;

select * from cidades c right join prefeitos p on c.id = p.cidade_id;

-- Ex de full join gambiarra

select * from cidades c left join prefeitos p on c.id = p.cidade_id
union
select * from cidades c right join prefeitos p on c.id = p.cidade_id;

