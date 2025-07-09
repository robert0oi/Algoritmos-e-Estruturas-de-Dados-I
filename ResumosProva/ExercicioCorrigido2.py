# Construa um algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos em ordem alfabética, uma função para imprimir os elementos da lista e uma função para imprimir os elementos na ordem inversa.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserir_ordenado(self, valor):
        novo_no = No(valor)
        
        if self.inicio is None:
            self.inicio = self.fim = novo_no
            self.tamanho += 1
            return
        
        if valor.lower() < self.inicio.valor.lower():
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no
            self.tamanho += 1
            return
        
        atual = self.inicio
        while atual.proximo and valor.lower() > atual.proximo.valor.lower():
            atual = atual.proximo
        
        novo_no.proximo = atual.proximo
        novo_no.anterior = atual
        
        if atual.proximo:
            atual.proximo.anterior = novo_no
        else:
            self.fim = novo_no
            
        atual.proximo = novo_no
        self.tamanho += 1
    
    def imprimir_ordem_direta(self):
        if self.inicio is None:
            print("Lista vazia")
            return
        
        atual = self.inicio
        print("Ordem direta:")
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")
    
    def imprimir_ordem_inversa(self):
        if self.fim is None:
            print("Lista vazia")
            return
        
        atual = self.fim
        print("Ordem inversa:")
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.anterior
        print("None")

if __name__ == "__main__":
    lista = ListaDuplamenteEncadeada()