# Exercicio de python básico
# Exemplo de input: 75.2
# Exemplo de output: 24.00

grausF = input("Digite a temperatura em graus Fahrenheit: ")
inp_casting = float(grausF)

conversao = 5 * ((inp_casting - 32) / 9)

print(f"A temperatura em graus Celsius que você me passou é: {conversao:.2f}c")