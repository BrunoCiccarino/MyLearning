"""Exercício 03.

Desenvolva uma classe que represente uma conta bancária com os seguintes atributos:
titular e saldo.
Adicione métodos para realizar operações de depósito e saque na conta.
Certifique-se de tratar casos onde o saldo pode se tornar negativo após um saque.
Após definir a classe, crie uma instância dela e realize algumas operações de depósito
e saque para verificar o funcionamento dos métodos implementados.
"""

class ContaBancaria:

    def __init__(self, titular: str, saldo: float) -> None:
        self.titular: str = titular
        self.saldo: float = saldo
    
    def deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print(f"Depositando {valor:.2f} na conta")
        else:
            print("Valor de deposito inválido")
        return self.saldo

    def saque(self, valor: float):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Sacado {valor:.2f}")
            else:
                print("Saque invalido ou saldo insuficiente!")
        else:
            print("Valor de saque invalido!")
        return self.saldo


conta_corrente = ContaBancaria(titular="Bruno", saldo=500)

novo_saldo = conta_corrente.deposito(250)
print(f"Saldo atual: {novo_saldo}") 

