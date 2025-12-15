from modelos.classes.aluno import Aluno
from modelos.classes.turma import Turma
from datetime import date
class Matricula:
    def __init__(self, aluno, turma):
        self.__aluno = aluno
        self.__turma = turma
        self.__nota = None
        self.__frequencia = None
        self.__ativa = True
        self.__data = date.today()
       
    @property
    def aluno(self):
        return self.__aluno

    @property
    def turma(self):
        return self.__turma

    def lancar_nota(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("Nota inválida")
        self.__nota = nota

    def lancar_frequencia(self, freq):
        if not 0 <= freq <= 100:
            raise ValueError("Frequência inválida")
        self.__frequencia = freq

    def calcular_situacao(self, settings):
        if not self.__ativa:
            return "TRANCADA"
        if self.__nota is None or self.__frequencia is None:
            return "CURSANDO"
        if self.__nota < settings.nota_minima:
            return "REPROVADO_POR_NOTA"
        if self.__frequencia < settings.frequencia_minima:
            return "REPROVADO_POR_FREQUENCIA"
        return "APROVADO"

    def trancar(self):
        self.__ativa = False

    def __eq__(self, other):
        if not isinstance(other, Matricula):
            return NotImplemented
        return self.__aluno.matricula == other.__aluno.matricula and self.__turma == other.__turma  
