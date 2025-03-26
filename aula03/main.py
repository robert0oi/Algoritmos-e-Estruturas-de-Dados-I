from Cidade import Cidade
from Pedido import Pedido
from Pessoa import Pessoa
from Produto import Produto

c1 = Cidade() #Itaquaquecetuba
c2 = Cidade("Porto Alegre")

p1 = Pessoa("João")
# p2 = Pessoa("Maria", None, c1)
p2 = Pessoa("Maria", cid = c1)

produto01 = Produto("Coca-Cola", 19.90)
produto02 = Produto("Guaraná Jesus", qtd = 50)
produto03 = Produto("Fanta Laranja", 18.75, 30)

pedido = Pedido(cli = p2)
pedido.addProduto(produto02)
pedido.addProduto(produto03)

print(pedido)