from abc import ABC, abstractmethod
from Categoria import Categoria

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return {
            'modelo': self.modelo,
            'cor': self.cor,
            'preco': self.preco,
            'categoria': (self.categoria.id, self.categoria.nome)
        }

    @abstractmethod
    def cadastrar(self):
        pass