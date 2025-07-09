class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adicionar(self, valor):
        novo_no = NoDuplo(valor)
        if self.fim is None:
            self.inicio = self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no