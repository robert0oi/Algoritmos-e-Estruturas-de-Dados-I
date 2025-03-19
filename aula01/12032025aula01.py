#Método que não possui parâmetros e nem retorno
def imprimirNomeProfessor():
    print("Adalto")

imprimirNomeProfessor()
# retornar != print

#Método


#Método



#Método


class Carro:
    def __init__(self, modelo, ano, quilometragem):
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def imprimirDados(self):
        print(f"Este é o modelo do veículo: {self.modelo}")
        print(f"Este é o ano do veículo: {self.ano}")
        print(f"Esta é a quilometragem do veículo: {self.quilometragem}")
    
    def incrementarKm(self):
        print(f"Esta é a sua quilometragem até o momento: {self.quilometragem}")
        kmAcrescentado = int(input("Digite quanto km deseja acrescentar a quilometragem do veículo: "))
        kmAtualizado = kmAcrescentado + self.quilometragem
        print(f"Esta é a nova quilometragem do veículo: {kmAtualizado}")

c1 = Carro("Honda Civic", 1995, 167.854)

c1.imprimirDados()
c1.incrementarKm()