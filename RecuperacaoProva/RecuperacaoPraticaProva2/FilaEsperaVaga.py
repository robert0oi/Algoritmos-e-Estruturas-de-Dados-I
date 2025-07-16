from Apartamento import Apartamento
import random

class FilaEsperaVaga:
    def __init__(self):
        self.id = None
        self.inicio = None
        self.fim = None

    def imprimirFila(self):
        print("\n" + "-" * 38 + "\n")
        if self.inicio == None:
            print("Fila de espera vazia.\n")
        else:
            aux = self.inicio
            txt = ""
            while aux != None:
                txtFila = str("="*10 + " Fila Espera Vaga " + "="*10 + "\n")
                txt += str(f"Apartamento {aux.numero}, Torre {aux.torre}.\n")
                aux = aux.prox 
            print(txtFila+txt)

    def AdicionarAptoFila(self, numero, torre):
        apartamento = Apartamento(numero, torre)
        if self.inicio == None:
            self.inicio = apartamento
        elif self.inicio.prox == None:
            self.inicio.prox = apartamento
        else:  
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = apartamento
        self.fim = apartamento
        print(f"\nApartamento {apartamento.numero}, Torre {apartamento.torre}, adicionado a fila.\n")

    def removerApto(self):
        vagaAleatoria = random.randint(1, 50)
        if self.inicio == None:
            print("\nFila de espera vazia.\n")
        elif self.inicio is not None:
            apartamentoRemovidoFila = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            print(f"Apartamento: {apartamentoRemovidoFila.numero} da Torre {apartamentoRemovidoFila.torre}.\nVaga atribuída: {vagaAleatoria}.")