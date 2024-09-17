"""Exercício 07.

Você está desenvolvendo um sistema para um hotel que permite aos clientes fazerem
reservas de quartos.
Crie uma classe chamada Quarto que represente um quarto do hotel.
Cada quarto deve ter um número, um tipo (por exemplo, simples, duplo, suíte), e um
status que indica se o quarto está disponível para reserva ou não.

    Adicione métodos à classe Quarto para reservar e liberar o quarto.
    Adicione um método para verificar se o quarto está disponível para reserva.

Crie alguns quartos diferentes e realize operações de reserva e liberação para testar a
funcionalidade.
"""

from typing import Literal


class Quarto:

    def __init__(self, numero: int, tipo: str, status: bool) -> None:
        self.numero: int = numero
        self.tipo: str = tipo
        self.status: bool = True # Dísponível

    def set_status(self) -> None:
        self.status = False
    
    def get_status(self) -> bool:
        return self.status
    
    def reserva(self) -> None:
        if self.status:
            print("Quarto reservado!")
            return self.set_status()
        
    def liberar_quarto(self) -> Literal[True] | Literal['Quarto liberado!']:
        if self.status != True:
            self.status = True
            return self.status
        return "Quarto liberado!"

quarto_1 = Quarto(numero=1, tipo="suíte", status=False)
print(quarto_1.liberar_quarto())
print(quarto_1.reserva())
