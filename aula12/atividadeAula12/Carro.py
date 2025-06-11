class Carro:
    def __init__(self, modelo, ano, cor, placa):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.prox = None  # Próximo carro na fila

    def __str__(self):
        return f"{self.modelo} ({self.ano}) - {self.cor} - Placa: {self.placa}"