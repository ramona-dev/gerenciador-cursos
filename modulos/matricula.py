import datetime
import settings

class Matricula:
    def __init__(self, aluno, turma):
        turma.adicionar_aluno(aluno, settings)  # valida regras antes
        self._aluno = aluno
        self._turma = turma
        self._nota = None
        self._frequencia = None
        self._ativa = True
        self._data = datetime.date.today()
        turma._matriculas[aluno] = self
        aluno._turmas.append(turma)

    @property
    def aluno(self):
        return self._aluno
    @property
    def turma(self):
        return self._turma

    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, valor: float):
        if valor is not None and not (0 <= valor <= 10):
            raise ValueError("Nota deve estar entre 0 e 10.")
        self._nota = valor

    @property
    def frequencia(self):
        return self._frequencia
    @frequencia.setter
    def frequencia(self, valor: float):
        if valor is not None and not (0 <= valor <= 100):
            raise ValueError("Frequência deve estar entre 0 e 100.")
        self._frequencia = valor

    @property
    def ativa(self):
        return self._ativa

    def lancar_nota(self, nota: float): 
        self.nota = nota
    def lancar_frequencia(self, freq: float):
        self.frequencia = freq

    def trancar(self):
        limite = settings.data_limite_trancamento
        hoje = datetime.date.today()
        if hoje <= limite:
            self._ativa = False
        else:
            raise ValueError("Prazo de trancamento expirado.")

    def situacao(self):
        if not self._ativa:
            return "TRANCADO"
        if self._nota is None or self._frequencia is None:
            return "CURSANDO"
        if self._frequencia < settings.frequencia_minima:
            return "REPROVADO_POR_FREQUENCIA"
        if self._nota < settings.nota_minima_aprovacao:
            return "REPROVADO_POR_NOTA"
        return "APROVADO"

    def __eq__(self, other):
        return (self._aluno.matricula == other._aluno.matricula) and (self._turma.id == other._turma.id)