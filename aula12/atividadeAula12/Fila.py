from Carro import Carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, valor):
        nodo = Carro(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.imprimir()
    
    def imprimir(self):
        print(("-" * 15) + " Fila - FIFO " + ("-" * 15))
        if self.inicio is None:
            print("A Fila está vazia!")
        else:
            aux = self.inicio
            txt = ""
            while aux: #ou aux is not None
                txt += aux.dado + " - "
                aux = aux.prox
            print(txt)

    def remover(self):
        if self.inicio is not None: # Verifica se a lista não está vazia
            elemento = self.inicio
            self.inicio = self.inicio.prox ##atencao
            if self.inicio == None:
                self.fim = None            
            print(carro.modelo, " Removido.")
        self.imprimir()