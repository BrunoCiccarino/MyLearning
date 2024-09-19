"""Exercício 02.

Desenvolva uma aplicação para gerenciar tarefas em um projeto.
Cada tarefa deve ser representada por uma dataclass contendo o nome da tarefa, sua
descrição e o status atual (por exemplo, "A Fazer", "Em Andamento" ou "Concluída").
Implemente uma classe Projeto e métodos para adicionar novas tarefas, alterar o status
das tarefas e listar todas as tarefas do projeto.
"""

from dataclasses import dataclass, field


@dataclass
class Tarefas:
    tarefas: list[str] = field(default_factory=list) 
    status: bool = False

    def get_tarefas(self) -> list:
        return self.tarefas
    
    def add_tarefas(self, tarefa) -> list:
        self.tarefas.append(f"{tarefa}")
        return self.tarefas
    
    def del_tarefas(self, tarefa) -> list:
        index = self.tarefas.index(tarefa)
        self.tarefas.pop(index)
        return self.tarefas

    def get_status(self) -> bool:
        return self.status
    
    def set_status(self) -> bool:
        self.status = True
        return self.status

tarefas = Tarefas(tarefas=[], status=False)
tarefas.add_tarefas(tarefa="limpar a casa")
tarefas.add_tarefas("limpar a louça")
tarefas.add_tarefas("ir pro curso")
tarefas.set_status()

print(tarefas)