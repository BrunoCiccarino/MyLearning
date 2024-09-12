"""Exercício 02.

Desenvolva uma classe chamada Calculadora que simule as operações básicas de uma
calculadora.
A classe deve conter métodos para adição, subtração, multiplicação e divisão.
Crie uma instância da classe Calculadora e realize algumas operações matemáticas
utilizando os métodos implementados.
    Exemplo de operações esperadas:
        5 + 3 = 8
        10 - 4 = 6
        2 * 6 = 12
        8 / 2 = 4.0
"""

class Calculadora:

    def __init__(self) -> None:
        pass

    def soma(self, num1, num2) -> int:
        return num1 + num2
    
    def subtracao(self, num1, num2) -> int:
        return num1 - num2
    
    def multiplicacao(self, num1, num2) -> int:
        return num1 * num2

    def divisao(self, num1, num2) -> int:
        return num1 / num2
    
calculadora = Calculadora()
print(calculadora.soma(5, 3))
print(calculadora.subtracao(10, 4))
print(calculadora.multiplicacao(2, 6))
print(calculadora.divisao(8, 2))
