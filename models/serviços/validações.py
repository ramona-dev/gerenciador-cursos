# Funções para verificar pré-requisitos, choques de horário, limite de vagas, limite de turmas por aluno
from modelos.classes.aluno import Aluno
from modelos.classes.matricula import Matricula
    

class MatriculaValidador:
    def __init__(self, settings):
        self.settings = settings

    def matricular(self, aluno, turma, matriculas_ativas):
        self._validar_turma(turma)
        self._validar_vagas(turma)
        self._validar_pre_requisitos(aluno, turma)
        self._validar_choque(aluno, turma, matriculas_ativas)
        self._validar_limite(aluno, matriculas_ativas)

        return Matricula(aluno, turma)
    
    def verificar_pre_requisitos(self, aluno: Aluno):
        for req in self.__curso._Curso__lista_requisitos:  # acessa lista de requisitos
            # checa se aluno tem aprovação no requisito
            aprovado = any(
                d["curso"] == req and d["nota"] >= self.__config.nota_minima and d["frequencia"] >= self.__config.frequencia_minima
                for d in aluno._Aluno__historico
            )
            if not aprovado:
                raise ValueError(f"Aluno não possui pré-requisito aprovado: {req}")

    def verificar_choque_horario(self, aluno: Aluno):
        # percorre turmas já matriculadas do aluno
        for turma in aluno._Aluno__turmas:
            for dia, intervalo in turma._Turma__horario.items():
                if dia in self.__horario:
                    if self.__horario[dia] == intervalo:
                        raise ValueError("Choque de horário detectado.")

    def verificar_limite_turmas(self, aluno: Aluno):
        if len(aluno._Aluno__turmas) >= self.__config.limite_turmas:
            raise ValueError("Aluno já atingiu o limite de turmas permitido.")

    def verificar_unicidade(self, aluno: Aluno):
        if aluno in self.__alunos_matriculados:
            raise ValueError("Aluno já matriculado nesta turma.")

    def matricular(self, aluno: Aluno):
        self.impedir_matricula_fech()
        if len(self.__alunos_matriculados) >= self.__capacidade:
            raise ValueError("Capacidade máxima atingida.")
        self.verificar_pre_requisitos(aluno)
        self.verificar_choque_horario(aluno)
        self.verificar_limite_turmas(aluno)
        self.verificar_unicidade(aluno)

        self.__alunos_matriculados.append(aluno)
        aluno._Aluno__turmas.append(self)  # adiciona turma ao aluno

    def __len__(self):
        return len(self.__alunos_matriculados)

    def relatorio_turma(self):
        relatorio = []
        for aluno in self.__alunos_matriculados:
            situacao = aluno.calcular_sit_matricula(
                nota_minima=self.__config.nota_minima,
                freq_minima=self.__config.frequencia_minima
            )
            cr = aluno.calculo_de_CR()
            relatorio.append(f"Aluno: {aluno.nome} | CR: {cr:.2f} | Situação: {situacao}")
        return "\n".join(relatorio)
