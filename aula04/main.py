import sys
from PyQt5.QtWidgets import QApplication
from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro
from TelaCategoria import TelaCategoria
from Categoria import Categoria

app = QApplication(sys.argv)

TelaVeiculo = TelaVeiculo("Cadastro de Veículo")
TelaVeiculo.show()

categorias = []
telaCat = TelaCategoria("Adicionar Categorias", categorias)



sys.exit(app.exec_())
