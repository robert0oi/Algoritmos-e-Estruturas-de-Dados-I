# retornar != print
#Método que tem retorno e não recebe parâmetro
def getPI():
    return 3.14
    
#Método que não tem retorno e não recebe parâmetro
def imprimirPI():
    print( getPI() )

#Método que tem retorno e recebe parâmetro
def calcularAreaCirculo(raio):
    area = getPI() * ( raio * raio )
    return area

#Método que não tem retorno e recebe parâmetro
def imprimirNomeProfessor():
    print("Adalto")

imprimirNomeProfessor()

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