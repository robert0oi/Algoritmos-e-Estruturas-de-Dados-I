from Produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potencia_da_fonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potencia_da_fonte  # Atributo fracamente privado

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        self._potenciaDaFonte = valor

    def getInformacoes(self):
        info = super().getInformacoes()
        info['potencia_da_fonte'] = self._potenciaDaFonte
        return info

    def cadastrar(self):
        print(f"Desktop {self.modelo} cadastrado!")