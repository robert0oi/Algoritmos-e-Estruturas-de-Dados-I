# 1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número do apartamento, número da vaga de garagem e torre.
# 2) Este condomínio, não possui vagas de garagem para todos os apartamentos. Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que contenha os métodos para adicionar apartamentos na fila, retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.
# 3) Construa um menu de opções ao usuário, com as funcionalidades do algoritmo.

import os # importar cls pra limpar tela
from Apartamento import Apartamento
from Torre import Torre
from FilaEsperaVaga import FilaEsperaVaga

def main():
    FilaApto = FilaEsperaVaga()

    while True:
        print("="*16 + " MENU " + "="*16)
        print("-"*8 + " (1) Adicionar na Fila " + "-"*7)
        print("-"*8 + " (2) Remover da Fila " + "-"*9)
        print("-"*8 + " (3) Status da Fila " + "-"*10)
        print("-"*8 + " (4) Sair " + "-"*20)
        print("="*38)

        opcao = input("Selecione a opção: ")
        if opcao == "1":
                numero = input("Número Apto: ")
                idTorre = input("ID da Torre: ")
                nomeTorre = input("Nome da Torre: ")
                enderecoTorre = input("Endereço da Torre: ")
                torre = Torre(idTorre, nomeTorre, enderecoTorre)
                FilaApto.AdicionarAptoFila(numero, torre)
        
        elif opcao == "2":
            FilaApto.removerApto()
        
        elif opcao == "3":
            FilaApto.imprimirFila()

        elif opcao == "4":
            print("Encerrando...")
            os.system('cls') # Limpa a tela
            break

        else:
            print("Opção inválida, digite novamente.")

if __name__ == "__main__":
