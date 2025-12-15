from .pessoa import Pessoa

class Aluno(Pessoa): 
    def __init__(self, matricula: str, nome: str, email: str):
        super().__init__(nome, matricula)
        self.__email = email
        self.__historico = []  # lista de dicts: {"curso": codigo, "nota": x, "frequencia": y}
        
    @property 
    def historico(self):
        return list(self.__historico)  # cópia

    def possui_aprovacao(self, codigo_curso, nota_min, freq_min):
        for d in self.__historico:
            if (
                d["curso"] == codigo_curso
                and d["nota"] >= nota_min
                and d["frequencia"] >= freq_min
            ):
                return True
        return False

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

    def __lt__(self, other):
        if not isinstance(other, Aluno):
            return NotImplemented
        if self.calculo_de_CR() == other.calculo_de_CR():
            return self.nome < other.nome
        return self.calculo_de_CR() < other.calculo_de_CR()