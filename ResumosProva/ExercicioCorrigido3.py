# Construa agora um algoritmo para implementação de um Pilha(LIFO) de Livros. Lembrando que na Pilha o último elemento adicionado, será o primeiro elemento removido.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.paginas} págs.)"

class PilhaLivros:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def empilhar(self, livro):
        novo_livro = {
            'livro': livro,
            'anterior': self.topo
        }
        self.topo = novo_livro
        self.tamanho += 1
        print(f"Livro '{livro.titulo}' adicionado à pilha!")
    
    def desempilhar(self):
        if self.topo is None:
            print("A pilha está vazia!")
            return None
        
        livro_removido = self.topo['livro']
        self.topo = self.topo['anterior']
        self.tamanho -= 1
        print(f"Livro removido: {livro_removido}")
        return livro_removido
    
    def mostrar_topo(self):
        if self.topo is None:
            print("A pilha está vazia!")
            return None
        
        return self.topo['livro']
    
    def imprimir_pilha(self):
        if self.topo is None:
            print("Pilha vazia!")
            return
        
        print("\n--- PILHA DE LIVROS --- (Topo para Base)")
        atual = self.topo
        while atual:
            print(atual['livro'])
            atual = atual['anterior']
        print(f"Total de livros: {self.tamanho}")
        print("----------------------")

def criar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    paginas = int(input("Número de páginas: "))
    return Livro(titulo, autor, paginas)

def menu():
    pilha = PilhaLivros()
    
    while True:
        print("\nMENU PILHA DE LIVROS")
        print("1. Adicionar livro (empilhar)")
        print("2. Remover livro (desempilhar)")
        print("3. Ver livro no topo")
        print("4. Mostrar todos os livros")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            livro = criar_livro()
            pilha.empilhar(livro)
        elif opcao == "2":
            pilha.desempilhar()
        elif opcao == "3":
            livro = pilha.mostrar_topo()
            if livro:
                print(f"Livro no topo: {livro}")
        elif opcao == "4":
            pilha.imprimir_pilha()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()