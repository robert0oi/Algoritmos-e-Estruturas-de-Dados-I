class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def enqueue(self, valor):
        novo_no = No(valor)
        if self.ultimo is None:
            self.primeiro = self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no
    
    def dequeue(self):
        if self.primeiro is None:
            return None
        temp = self.primeiro
        self.primeiro = temp.proximo
        if self.primeiro is None:
            self.ultimo = None
        return temp.dado