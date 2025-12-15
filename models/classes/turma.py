from modelos.classes.oferta import Oferta
from modelos.classes.curso import Curso

class Turma(Oferta):
    def __init__(self, id_turma, curso, periodo, horario, capacidade):
        self.__id = id_turma
        self.__curso = curso
        self.__periodo = periodo
        self.__horario = horario  # dict dia -> (inicio, fim)
        self.__capacidade = capacidade
        self.__matriculas = []
        self.__aberta = True

    def adicionar_matricula(self, matricula):
        if not self.esta_aberta():
            raise ValueError("Turma fechada")
        if not self.possui_vaga():
            raise ValueError("Turma lotada")
        self.__matriculas.append(matricula)

    def possui_vaga(self):
        return len(self) < self.__capacidade

    def horarios(self):
        return self.__horario

    def esta_aberta(self):
        return self.__aberta

    def abrir(self):
        self.__aberta = True

    def fechar(self):
        self.__aberta = False

    def __len__(self):
        return len(self.__matriculas)