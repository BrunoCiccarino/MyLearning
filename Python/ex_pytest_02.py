"""Exercício 02.

Você esteja desenvolvendo um aplicativo de análise de dados e precise testar uma
função que calcula a média de uma lista de valores.
Escreva testes usando pytest para garantir que a função calcula a média corretamente
para diferentes conjuntos de dados.
"""

from main import calcula_numeros

def test_lista():
    assert calcula_numeros(numeros=[]) == None
    assert calcula_numeros([1,2,3,4,5]) == 3.0
    assert calcula_numeros([1.1,1.2,1.3,1.4,1.5]) == 1.3