import collections

def queue():
    d = collections.deque([9,8,7,6,5,4]) # Inicializo a fila com uma lista de 9 a 4
    return d 

d = queue()
print("Deque",d) # Printo o valor da lista da fila

def insertQueue(): # Adiciono o valor 1 2 3 na lista da fila
    d.append(1) 
    d.append(2)
    d.append(3)

def removeQueue(): # Removo o primeiro item na lista da fila
    d.popleft()

insert = insertQueue()
print("Adding 3, 2, 1",d)

remove = removeQueue()
print("Removing 9 from deque", d)