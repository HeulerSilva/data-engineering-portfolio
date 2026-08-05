select cliente, data, nome as vendedor, produto, quantidade as qt, total
into fatovendas
from vendas v
inner join clientes c on (c.idcliente = v.idcliente)
inner join itensvenda i on (i.idvenda = v.idvenda)
inner join produtos p on (p.idproduto = i.idproduto)
inner join vendedores vn on (vn.idvendedor = v.idvendedor);