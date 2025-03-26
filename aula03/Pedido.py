from Pessoa import Pessoa
from Produto import Produto
from datetime import date

class Pedido:
    def __init__(self, data = date.today(), cli = Pessoa("Balcão")):
        self.id = None
        self.data = data
        self.cliente = cli
        self.produtos = []

    def addProduto(self, produto): #sem esquecer o self
        if produto != None and produto.preco >= 10:
            self.produtos.append(produto)
        soma = 0.0
        for p in self.produtos:
            soma += p.preco #atenção
        return soma

    def __str__(self):
        txt = "Pedido Realizado em: " + str(self.data)
        # txt += "\nCliente: " + self.cliente.nome #Curiosidade
        txt += "\nCliente: " + str(self.cliente)
        txt += "\nProdutos: "
        for p in self.produtos:
            txt += str(p)
            txt += "\n--------------------\n"
        return txt
