class Cidade:
    def __init__(self, name = "Itaquaquecetuba"):
        self.id = None
        self.nome = name

    def __str__(self):
        return "Id: " + str(self.id) + " - " + self.nome
