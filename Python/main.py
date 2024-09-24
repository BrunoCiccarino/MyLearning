
def calcula_numeros(numeros):
    if not numeros:
        return None
    
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print(calcula_numeros([1.1,1.2,1.3,1.4,1.5]))