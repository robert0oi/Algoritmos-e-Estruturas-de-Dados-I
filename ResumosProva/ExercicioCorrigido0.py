# Implemente uma Pilha de livros e uma Lista Encadeada de autores. A lista de autores deve conter os autores ordenados pelo nome do autor.
# A classe Livro deve conter os atributos:
# título: String
# autor: Autor
# páginas: int
# A classe Autor deve conter os atributos:
# nome: String
# nacionalidade: String
# Monte um menu que permita adicionar e remover livros, adicionar autores e imprimir a lista de autores e a pilha de livros.

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
    
    def __str__(self):
        return f"{self.nome} ({self.nacionalidade})"

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor.nome}, {self.paginas} págs."

class NoAutor:
    def __init__(self, autor):
        self.autor = autor
        self.proximo = None

class ListaAutores:
    def __init__(self):
        self.cabeca = None
    
    def adicionar_autor(self, autor):
        novo_no = NoAutor(autor)
        
        if self.cabeca is None or autor.nome < self.cabeca.autor.nome:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None and atual.proximo.autor.nome < autor.nome:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
    
    def imprimir_autores(self):
        atual = self.cabeca
        print("\n--- LISTA DE AUTORES ---")
        while atual is not None:
            print(atual.autor)
            atual = atual.proximo
        print("-----------------------\n")

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
    
    def desempilhar(self):
        if self.topo is None:
            return None
        livro_removido = self.topo['livro']
        self.topo = self.topo['anterior']
        self.tamanho -= 1
        return livro_removido
    
    def imprimir_pilha(self):
        atual = self.topo
        print("\n--- PILHA DE LIVROS ---")
        while atual is not None:
            print(atual['livro'])
            atual = atual['anterior']
        print(f"Total: {self.tamanho} livros")
        print("----------------------\n")

def main():
    lista_autores = ListaAutores()
    pilha_livros = PilhaLivros()
    
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Adicionar autor")
        print("2. Listar autores")
        print("3. Adicionar livro")
        print("4. Remover livro (do topo)")
        print("5. Listar livros")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade: ")
            novo_autor = Autor(nome, nacionalidade)
            lista_autores.adicionar_autor(novo_autor)
            print(f"Autor {nome} adicionado com sucesso!")
        
        elif opcao == "2":
            lista_autores.imprimir_autores()
        
        elif opcao == "3":
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            
            atual = lista_autores.cabeca
            autor_encontrado = None
            while atual is not None:
                if atual.autor.nome == nome_autor:
                    autor_encontrado = atual.autor
                    break
                atual = atual.proximo
            
            if autor_encontrado:
                try:
                    paginas = int(input("Número de páginas: "))
                    novo_livro = Livro(titulo, autor_encontrado, paginas)
                    pilha_livros.empilhar(novo_livro)
                    print(f"Livro '{titulo}' adicionado à pilha!")
                except ValueError:
                    print("Número de páginas deve ser um valor inteiro!")
            else:
                print(f"Autor '{nome_autor}' não encontrado! Adicione o autor primeiro.")
        
        elif opcao == "4":
            livro_removido = pilha_livros.desempilhar()
            if livro_removido:
                print(f"Livro removido: {livro_removido}")
            else:
                print("A pilha de livros está vazia!")
        
        elif opcao == "5":
            pilha_livros.imprimir_pilha()
        
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

# Maneira mais simples: ---------------------------------------------------

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

pilha_livros = []

lista_autores = []

def adicionar_autor():
    nome = input("Nome do autor: ")
    nacionalidade = input("Nacionalidade: ")
    lista_autores.append(Autor(nome, nacionalidade))
    lista_autores.sort(key=lambda x: x.nome)
    print(f"Autor {nome} adicionado!")

def listar_autores():
    print("\nAutores cadastrados:")
    for autor in lista_autores:
        print(f"- {autor.nome} ({autor.nacionalidade})")

def adicionar_livro():
    titulo = input("Título do livro: ")
    nome_autor = input("Nome do autor: ")
    
    autor_encontrado = None
    for autor in lista_autores:
        if autor.nome == nome_autor:
            autor_encontrado = autor
            break
    
    if autor_encontrado:
        paginas = int(input("Número de páginas: "))
        pilha_livros.append(Livro(titulo, autor_encontrado, paginas))
        print(f"Livro '{titulo}' empilhado!")
    else:
        print("Autor não encontrado!")

def remover_livro():
    if pilha_livros:
        livro = pilha_livros.pop()
        print(f"Livro removido: {livro.titulo}")
    else:
        print("A pilha está vazia!")

def listar_livros():
    print("\nLivros na pilha (do topo para a base):")
    for livro in reversed(pilha_livros):
        print(f"- '{livro.titulo}' por {livro.autor.nome}, {livro.paginas} págs.")

while True:
    print("\nMENU:")
    print("1. Adicionar autor")
    print("2. Listar autores")
    print("3. Adicionar livro")
    print("4. Remover livro (do topo)")
    print("5. Listar livros")
    print("6. Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        adicionar_autor()
    elif opcao == "2":
        listar_autores()
    elif opcao == "3":
        adicionar_livro()
    elif opcao == "4":
        remover_livro()
    elif opcao == "5":
        listar_livros()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")