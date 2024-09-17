"""Exercício 06.

Em uma escola, você precisa gerenciar informações sobre os alunos.
Crie uma classe chamada Aluno que represente um estudante.
Cada aluno deve ter um nome, uma idade e uma lista de disciplinas em que está
matriculado.

    Adicione métodos à classe Aluno para adicionar e remover disciplinas da lista.
    Adicione um método para verificar se um aluno está matriculado em uma determinada
    disciplina.

Crie alguns alunos e realize operações de matrícula e remoção de disciplinas para
testar a funcionalidade.
"""

class Aluno:

    def __init__(self, nome: str, idade: int, materias: list) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.materias: list = [materias]

    def get_nome(self) -> str:
        return self.__nome
    
    def get_idade(self) -> int:
        return self.__idade
    
    def get_materias(self) -> list:
        return self.materias
    
    def set_materias(self, materia_e) -> list:
        self.materias.append(f"{materia_e}")
        return self.materias
    
    def remove_materias(self, materia_r) -> list:
        index = self.materias.index(materia_r)
        self.materias.pop(index)
        return self.materias

    
aluno1 = Aluno(nome="Bruno", idade=20, materias=[])
aluno1.set_materias("matemática")
aluno1.set_materias("física")
aluno1.set_materias("biologia")
print(aluno1.get_nome())
print(aluno1.get_idade())
print(aluno1.get_materias())
print(aluno1.set_materias("ed-física"))
print(aluno1.remove_materias("matemática"))
