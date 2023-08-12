select * from estados


select sigla, nome as 'Estado Federativo'  from estados


select nome, regiao from estados
where populacao >= 10
order by populacao desc