# Exercicio de conversão de graus celsius para farenheit

graus = input("Digite a temperatura em graus celsius: ")
inp_casting = float(graus)

conversao = (inp_casting * 1.8) + 32

print(f"A temperatura em graus Fahrenheit que você me passou é: {conversao:.2f}f")