# Um exercicio que eu fiz para o Livro Entendendo Algoritmos - Um Guia Ilustrado Para Programadores e Outros Curiosos 

low = 0
high = 24
x = int(input("Digite o número que você quer encontrar na lista: "))
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

"""
A busca binária é uma maneira simples e rápida de encontrar um valor dentro de um array por eliminação
algoritmo funciona dividindo o arranjo no meio repetidamente e comparando o elemento no meio com o elemento procurado.
o low que eu declarei ali em cima é o valor mínimo e o high é o valor máximo, o x é o valor que eu quero encontrar dentro do array
"""

while low < high:
    mid = low + (high - low) / 2
    int_mid = int(mid)

    if lista[int_mid] == x:
        print(int_mid)
        break
    elif x < lista[int_mid]:
        high = int_mid
    else:
        low = int_mid + 1

