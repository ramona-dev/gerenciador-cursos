from datetime import date

# Classe base
class Pessoa:
    def __init__(self, nome: str, matricula: str):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    def validar_cadastro(self):
        return bool(self.__nome and self.__matricula)


class Aluno(Pessoa):
    def __init__(self, matricula: str, nome: str, email: str):
        super().__init__(nome, matricula)
        self.__email = email
        self.__historico = []  # lista de dicts: {"curso": codigo, "nota": x, "frequencia": y}

    @property
    def email(self):
        return self.__email

    def adicionar_disciplina(self, curso, nota: float, frequencia: float):
        if not (0 <= nota <= 10):
            raise ValueError("Nota deve estar entre 0 e 10.")
        if not (0 <= frequencia <= 100):
            raise ValueError("Frequência deve estar entre 0 e 100.")
        self.__historico.append({"curso": curso.codigo, "nota": nota, "frequencia": frequencia})

    def calculo_de_CR(self):
        if not self.__historico:
            return 0
        return sum(d["nota"] for d in self.__historico) / len(self.__historico)

    def calcular_sit_matricula(self, nota_minima=6.0, freq_minima=75.0):
        for d in self.__historico:
            if d["nota"] < nota_minima:
                return "REPROVADO_POR_NOTA"
            if d["frequencia"] < freq_minima:
                return "REPROVADO_POR_FREQUENCIA"
        return "APROVADO"

    def __lt__(self, other):
        if not isinstance(other, Aluno):
            return NotImplemented
        if self.calculo_de_CR() == other.calculo_de_CR():
            return self.nome < other.nome
        return self.calculo_de_CR() < other.calculo_de_CR()


class Professor(Pessoa):
    def __init__(self, matricula_prof: str, nome: str, historico=None):
        super().__init__(nome, matricula_prof)
        self.__historico = historico or []


class Curso:
    def __init__(self, codigo_curso: str, nome: str, carga_horaria: int, lista_requisitos=None, disciplinas=None):
        self.__codigo_curso = codigo_curso
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__lista_requisitos = lista_requisitos or []
        self.__disciplinas = disciplinas or []

    @property
    def codigo(self):
        return self.__codigo_curso

    def calcular_carga_horaria(self):
        return self.__carga_horaria

    def impedir_ciclos(self, outro_curso):
        if outro_curso.codigo == self.__codigo_curso:
            raise ValueError("Um curso não pode ser pré-requisito de si mesmo.")

    def __str__(self):
        return f"Curso {self.__codigo_curso} - {self.__nome} ({self.__carga_horaria}h)"


class Oferta:
    def __init__(self, id_oferta: str, codigo_curso: str, periodo: str):
        self.__id_oferta = id_oferta
        self.__codigo_curso = codigo_curso
        self.__periodo = periodo


class Turma(Oferta):
    def __init__(self, id_turma: str, codigo_curso: str, periodo: str, horario: dict, sala: str, capacidade: int):
        super().__init__(id_turma, codigo_curso, periodo)
        self.__horario = horario
        self.__sala = sala
        self.__capacidade = capacidade
        self.__alunos_matriculados = []
        self.__aberta = True

    def abrir_turma(self):
        self.__aberta = True

    def fechar_turma(self):
        self.__aberta = False

    def impedir_matricula_fech(self):
        if not self.__aberta:
            raise ValueError("Turma está fechada.")

    def matricular(self, aluno):
        self.impedir_matricula_fech()
        if len(self.__alunos_matriculados) >= self.__capacidade:
            raise ValueError("Capacidade máxima atingida.")
        self.__alunos_matriculados.append(aluno)

    def __len__(self):
        return len(self.__alunos_matriculados)


class Configuracoes:
    def __init__(self, nota_minima: float, frequencia_minima: float, top_n_alunos: int, limite_turmas: int):
        self.nota_minima = nota_minima
        self.frequencia_minima = frequencia_minima
        self.top_n_alunos = top_n_alunos
        self.limite_turmas = limite_turmas

    def carregar_arquivo(self, caminho="settings.json"):
        # Implementar leitura de JSON futuramente
        pass


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


# Teste de uso 
if __name__ == "__main__":
    curso_python = Curso("CS101", "Python Básico", 60)
    turma_python = Turma("T1", curso_python.codigo, "2025.2", {"ter": "10:00-12:00"}, "Lab 01", 2)

    aluno1 = Aluno("2025001", "Ramona", "ramona@email.com")
    aluno2 = Aluno("2025002", "Carlos", "carlos@email.com")

    turma_python.matricular(aluno1)
    turma_python.matricular(aluno2)
    turma_python = relatorio_turma

    aluno1.adicionar_disciplina(curso_python, nota=8.5, frequencia=90)
    aluno2.adicionar_disciplina(curso_python, nota=5.0, frequencia=80)

    print("Relatório da Turma:")
    print(turma_python.relatorio_turma())

