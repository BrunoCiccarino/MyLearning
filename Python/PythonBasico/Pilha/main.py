# Exercicio aprendendo estrutura de dados, hoje estou fazendo uma representação de uma pilha

import collections

class CallStack:
    def __init__(self):
        self.d = collections.deque()

MyDeque = CallStack()

def insertQueue():
    MyDeque.d.append(1)
    MyDeque.d.append(2)
    MyDeque.d.append(3)
    MyDeque.d.append(4)
    MyDeque.d.append(5)


def removeQueue():
    MyDeque.d.pop()

insert = insertQueue()
print("inserting items into the stack: ", MyDeque.d)
remove = removeQueue()
print("Removing the last item from the stack: ", MyDeque.d)