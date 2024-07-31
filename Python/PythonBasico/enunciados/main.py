"""
Curso do Luiz Otávio Miranda: Python do básico ao avançado com projetos reais
Exercicio: Enunciado
"""

num1 = input("Digite um número e eu digo se ele é inteiro ou não: ")
try:
    num1_int = int(num1)

    if (num1_int % 2 == 0):
        print("O número é par")
    else: 
        print("O número é impar")
except ValueError:
    print("Digite um número inteiro")
    
horario = input("Digite que horas são: ")
horario_int = int(horario)

if horario_int > 0 and horario_int <= 11:
    print(f"Bom dia! Ja são {horario_int} horas.")
elif horario_int >= 12 and horario_int <= 17:
    print(f"Boa tarde! Ja são {horario_int} horas.")
elif horario_int >= 18 and horario_int <= 23:
    print(f"Boa noite! Ja são {horario_int} horas.")
else:
    print("Digite um horario válido")

nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) <= 6:
    print("Seu nome é normal!")
elif len(nome) > 6:
    print("Seu nome é muito grande!")

