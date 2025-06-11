from Carro import Carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, carro):
        if self.inicio is None:
            self.inicio = carro
        else:
            self.fim.prox = carro
        self.fim = carro
        self.imprimir()

    def imprimir(self):
        print(("-" * 16) + " Lavagem de Carros " + ("-" * 15))
        if self.inicio is None:
            print("A fila está vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux)
                aux = aux.prox

    def remover(self):
        if self.inicio is not None:
            removido = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            print(f"Carro Lavado: {removido}")
        else:
            print("A fila está vazia!")
        self.imprimir()
