from Produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempo_de_bateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempo_de_bateria  # Atributo fortemente privado, mas é só para mostrar, pois não é um atributo privado realmente

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        self.__tempoDeBateria = valor

    def getInformacoes(self):
        info = super().getInformacoes()
        info['tempo_de_bateria'] = self.__tempoDeBateria
        return info

    def cadastrar(self):
        print(f"Notebook {self.modelo} cadastrado!")