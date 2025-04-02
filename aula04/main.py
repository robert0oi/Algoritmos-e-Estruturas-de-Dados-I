import sys
from PyQt5.QtWidgets import QApplication
from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro

app = QApplication(sys.argv)

TelaVeiculo = TelaVeiculo("Cadastro de Veículo")
TelaVeiculo.show()

sys.exit(app.exec_())
