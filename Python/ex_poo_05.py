"""Exercício 05.

Você é responsável por desenvolver um sistema de gestão de estoque para uma loja.
Crie uma classe chamada Produto que represente um item em estoque.
Cada produto deve ter um nome, um preço e uma quantidade disponível em estoque.

    Adicione métodos à classe Produto para aumentar e diminuir a quantidade em estoque.
    Adicione um método para calcular o valor total do estoque de um produto
    (preço * quantidade).

Crie dois produtos diferentes e realize algumas operações para demonstrar o
funcionamento do sistema.
"""

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        self.nome: str = nome
        self.preco: float = preco
        self.quantidade: int = quantidade

    def get_quantidade(self):
        self.quantidade = []
        return self.quantidade
    
    def aumenta(self):
        self.quantidade += 1
        return self.quantidade
    
    def diminui(self):
        self.quantidade -= 1
        return self.quantidade
    
    def valor_estoque(self):
        return self.quantidade * self.preco
    
tomate = Produto(nome="Tomate", preco=5.8, quantidade=5)
laranja = Produto(nome="Laranja", preco=3.4, quantidade=10)

print(tomate.aumenta())
print(laranja.aumenta())
print(tomate.diminui())
print(laranja.diminui())
print(tomate.valor_estoque())
print(laranja.valor_estoque())
