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

