import os
from Fila import Fila
from Carro import Carro

fila = Fila()
op = -1

while op != 0:
    os.system('cls')
    print("-" * 50)
    print("1 - Adicionar Carro na Fila")
    print("2 - Remover da Fila")
    print("3 - Imprimir Fila")
    print("0 - Sair")
    op = int(input("Digite sua opção: "))
    
    if op == 1:
        modelo = str(input("Modelo do carro: "))
        ano = str(input("Ano do carro: "))
        cor = str(input("Cor do carro: "))
        placa = str(input("Placa do carro: "))
        carro = Carro(modelo, ano, cor, placa)
        fila.add(carro)
    
    elif op == 2:
        fila.remover()
    
    elif op == 3:
        fila.imprimir()
    
    elif op != 0:
        print("Opção inválida!")

    input("ENTER para continuar...")