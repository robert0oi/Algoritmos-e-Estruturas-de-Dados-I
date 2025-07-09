# Utilize o projeto desenvolvido em aula e adicione a função que armazena os valores em ordem crescente.

from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def adicionar_ordenado(self, valor):
        novo_no = No(valor)
        
        if self.inicio is None:
            self.inicio = novo_no
            self.tamanho += 1
            return
        
        if valor < self.inicio.dado:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
            self.tamanho += 1
            return
        
        anterior = self.inicio
        atual = self.inicio.proximo
        
        while atual is not None and valor > atual.dado:
            anterior = atual
            atual = atual.proximo
        
        novo_no.proximo = atual
        anterior.proximo = novo_no
        self.tamanho += 1
    
    def adicionar(self, valor):
        if self.inicio:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = No(valor)
        else:
            self.inicio = No(valor)
        self.tamanho += 1
    
    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado, end=" -> ")
                aux = aux.proximo
            print("None")
            print("Tamanho da Lista:", self.tamanho)
    
    def excluir(self, valor):
        if self.tamanho == 0:
            print("A lista está vazia")
        elif self.tamanho == 1:
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho -= 1
            else:
                print("Valor não encontrado")
        else:
            if self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            else:
                anterior = self.inicio
                atual = self.inicio.proximo
                while atual:
                    if atual.dado == valor:
                        anterior.proximo = atual.proximo
                        self.tamanho -= 1
                        return
                    anterior = atual
                    atual = atual.proximo
                print("Valor não encontrado")