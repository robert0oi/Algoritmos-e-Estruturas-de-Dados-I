# Construa um algoritmo que possua uma tupla com os números escritos por extenso de “zero” a “nove”. Peça ao usuário para digitar um número de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas condicionais (if e switch).

numerosExtenso = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove"
)

try:
    numero = int(input("Digite um número de 0 a 9: "))
    print(f"O número por extenso é: {numerosExtenso[numero]}")
except (ValueError, IndexError):
    print("Valor inválido! Digite apenas números de 0 a 9.")