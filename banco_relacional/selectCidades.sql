select es.nome, es.regiao, ci.nome from estados as es, cidades as ci
where es.id = ci.estado_id;