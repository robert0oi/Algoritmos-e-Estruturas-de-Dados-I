from No import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    
    def addNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            nodo.prox = self.inicio
            self.inicio = nodo
        self.imprimir()

    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            if self.inicio.prox is None:
                self.inicio.prox = nodo
            else: #Caí aqui, então a lista tem mais de um número.
                aux = self.inicio.prox 
                while aux.prox is not None:
                    aux = aux.prox 
                aux.prox = nodo
        self.imprimir()
    
    def imprimir(self):
        print("-" * 30)
        if self.inicio is None:
            print("Lista Encadeada está vazia!")
        else:
            aux = self.inicio
            while aux: #ou aux is not None
                print(aux.dado)
                aux = aux.prox

    def removerDoInicio(self):
        if self.inicio is not None: #Verificar se a lista não está vazia.
           # if self.inicio.prox == None: #Caso a lista tenha somente um elemento.
                #self.inicio = None
            #else: #Caso a lista tenha mais que um elemento.
            self.inicio = self.inicio.prox ##atencao
            print("Elemento Removido")
        self.imprimir()


    def removerDoFim(self):
        if self.inicio is not None:
            if self.inicio.prox == None:
                self.inicio = None
            else: #Cai aqui se tiver mais q um elemento
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox: #while aux.prox != None: # Se o valor do último.próximo for nulo, o laço para.
                    ant = aux
                    aux = aux.prox
                ant.prox = None # Aqui o penúltimo.próximo receberá None, já que queremos excluir o último. 
            print("Elemento Removido")
        self.imprimir()

    def remover(self, valor): # Remover Específico
        if self.inicio != None:
            removeu = False
            if self.inicio.dado == valor:
                self.incio = self.incio.prox ##atencao
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux != None: # while aux: (for um valor válido)
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                    else:
                        ant = aux
                        aux = aux.prox
                if removeu:
                    print(f"Elemento ${valor} removido")
                else:    
                    print("Elemento Não Encontrado")
        self.imprimir()