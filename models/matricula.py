class Matricula:
    def __init__(self, aluno: Aluno, turma: Turma):
        self.__aluno = aluno
        self.__turma = turma
        self.__data = date.today()
        self.__ativa = True

    def desistir(self):
        self.__ativa = False

    def __eq__(self, other):
        if not isinstance(other, Matricula):
            return NotImplemented
        return self.__aluno.matricula == other.__aluno.matricula and self.__turma == other.__turma  
